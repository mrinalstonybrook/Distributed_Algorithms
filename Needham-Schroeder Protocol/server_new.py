#!/usr/bin/env python

import crypto
import json
import socket
import threading
from Crypto.PublicKey import RSA
from colorama import Fore, Back, Style

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

class Server_proto(threading.Thread):

   def __init__(self, server_key,threadLock):
        threading.Thread.__init__(self)
        self.lock = threadLock
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_key = server_key
        self.connection_socket_list = {}
        self.client_addr_list = {}

        self.client_guid = None
        self.server_guid = None
        self.expires = None 
        self.client_public_keys = {}
        self.client_key_fingerprint = {}
   
   def load_client_keys(self):
        alice_key =   crypto.load_key_file('alicekey.pem') 
        self.client_public_keys['alice'] = alice_key.publickey().exportKey()
        self.client_key_fingerprint['alice'] = crypto.public_key_fingerprint(alice_key.publickey())

        bob_key =   crypto.load_key_file('bobkey.pem') 
        self.client_public_keys['bob'] = bob_key.publickey().exportKey()
        self.client_key_fingerprint['bob'] = crypto.public_key_fingerprint(bob_key.publickey())

   def bind_to_port(self,(tcp_ip,tcp_port)):
        self.server_socket.bind((tcp_ip, tcp_port))

   def start_to_listen(self):
        self.server_socket.listen(2)
   
   def send_message_to_client(self,msg,client_name):
        self.connection_socket_list[client_name].send(msg)

   def register_client(self,client_name,client_public_key):
        self.client_public_keys[client_name] = client_public_key

   def recv_message_from_client(self,client_name):
        return self.connection_socket_list[client_name].recv(BUFFER_SIZE)

   def session_key(self):
        return "%s:%s" % (self.client_guid, self.server_guid) 
   
   def accept_connection(self,client_name):
        temp_connection_socket , temp_client_addr = self.server_socket.accept()
        self.connection_socket_list[client_name] = temp_connection_socket
        self.client_addr_list[client_name] = temp_client_addr


   def send_public_key(self,client_name_req,client_name):
        print('Sending ' + client_name + '\'s public key')
        self.connection_socket_list[client_name].send(self.client_public_keys[client_name_req].publickey().exportKey())

   def close_connection(self,client_name):
        self.connection_socket_list[client_name].close()

   def run(self):
       self.lock.acquire()
       self.bind_to_port((TCP_IP, TCP_PORT))
       self.load_client_keys()

       print('Starting the Server\n\n')
        
       self.start_to_listen()
       self.lock.release()

       self.accept_connection('alice')      

       #print ('Connection address:', self.client_addr_list['alice'])
       while 1:
           msg_a = self.recv_message_from_client('alice')
           if not msg_a: break
           msg_list_a = msg_a.split(':')
           if(msg_list_a[0] == 'get_client_address'):
             print(Fore.RED + 'Step 2: \n\n')
             print(Fore.WHITE +'Server ->'+ ' Alice : Sending Bob\'s public key and identity ')
             jmsg_a = {'key': self.client_key_fingerprint['bob'] , 'identity': 'bob'}
             jmsg_a_txt = json.dumps(jmsg_a)
             #print('length of text' + str(len(jmsg_a_txt)))
             #jmsg_a_txt_encrypt = crypto.rsa_encrypt(jmsg_a_txt, self.server_key)
             jmsg_a_txt_encrypt = self.server_key.encrypt(jmsg_a_txt,1)
             self.send_message_to_client(jmsg_a_txt_encrypt[0],'alice')
       self.close_connection('alice')

       #print('Connecting to Bob')

       #server.start_to_listen()
       self.accept_connection('bob')
       #server.load_client_keys()

       #print ('Connection address:', self.client_addr_list['bob'])
       while 1:
           msg_b = self.recv_message_from_client('bob')
           if not msg_b: break
           msg_list_b = msg_b.split(':')
           if(msg_list_b[0] == 'get_client_address'):
             print(Fore.RED + 'Step 4: \n\n')
             print(Fore.WHITE + 'Server ->'+ ' Bob : Sending Alice\'s public key and identity ')
             jmsg_b = {'key': self.client_key_fingerprint['alice'] , 'identity': 'alice'}
             jmsg_b_txt = json.dumps(jmsg_b)
             jmsg_b_txt_encrypt = self.server_key.encrypt(jmsg_b_txt,1)
             self.send_message_to_client(jmsg_b_txt_encrypt[0],'bob')
       self.close_connection('bob')




