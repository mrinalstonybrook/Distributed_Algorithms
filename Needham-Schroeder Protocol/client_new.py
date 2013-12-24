#!/usr/bin/env python
import crypto 
import json
import socket
import threading
from Crypto.PublicKey import RSA
from colorama import Fore, Back, Style

BUFFER_SIZE = 1024
TCP_IP = '127.0.0.1'
TCP_SERVER_PORT = 5005
TCP_PEER_PORT = 5006

class Client_proto(threading.Thread):

   def __init__(self, client_name,peer_name,context,client_key, server_key,threadLock):
        threading.Thread.__init__(self)
        self.lock = threadLock
        self.context = context
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_key = client_key
        self.server_key = server_key
        self.client_name = client_name
        self.peer_name = peer_name
        self.peer_key = None

        self.server_key_fprint = crypto.public_key_fingerprint(self.server_key)
        self.client_key_fprint = crypto.public_key_fingerprint(self.client_key) 
  
        self.client_guid = None
        self.peer_guid = None
        self.server_guid = None
        self.expires = None

# varaibles to be used when the client behaves as server
        self.server_socket_2 = None
        self.server_key_2 = None  
        self.connection_socket_list_2 = {}
        self.client_addr_list_2 = {}

   def connect_to_port(self,(tcp_ip, tcp_port)):
        self.client_socket.connect((tcp_ip, tcp_port))
   
   def send_message_to_server(self,msg):
        self.client_socket.send(msg)

   def send_dict_message_to_server(self,k):
        as_json = json.dumps(k)
        self.client_socket.send(as_json)

   def recv_message_from_server(self):
        return self.client_socket.recv(BUFFER_SIZE)

   def close_client_connection(self):
        return self.client_socket.close()

   def session_key(self):
        return "%s:%s" % (self.client_guid, self.server_guid)  

   def get_hello_message(self):
        self.client_guid = crypto.random_guid()

        hello_message = {"client_guid": self.client_guid,
                         "client_key_fingerprint": self.client_key_fprint}

        return hello_message

   def get_message(self):
        self.client_guid = crypto.random_guid()

        hello_message = {"NA": self.client_guid,
                         "A": self.client_key_fprint}

        return hello_message

   def process_hello_response(self, response):
        # Check the server send back the client_guid we sent.
        if response["client_guid"] != self.client_guid:
            message = ("Server did not send back the expected client_guid. "
                       "Expected: %s, Got: %s" %
                       (self.client_guid, response["client_guid"]))
            raise ProtocolError(message)

        # Check the server's stated fingerprint matches the one we know
        if response["server_key_fingerprint"] != self.server_key_fprint:
            message = ("Server did not send back the expected key fingerprint. "
                       "Expected: %s, Got: %s" %
                       (self.server_key_fprint,
                        response["server_key_fingerprint"]))
            raise ProtocolError(message)

        self.expires = response["expires"]
        self.server_guid = response["server_guid"]


   def get_confirmation_message(self):
        confirm_message = {"server_guid": self.server_guid}
        return confirm_message


   def encrypt_for_server(self, message):
        as_json = json.dumps(message)
        return crypto.rsa_encrypt(as_json, self.server_key)


   def decrypt_from_server(self, encrypted):
        decrypted = crypto.rsa_decrypt(encrypted, self.client_key)
        return json.loads(decrypted)

# here is the functionality of the server to implemneted on the client side 

   def bind_to_port(self,(tcp_ip,tcp_port)):
        self.server_socket_2 = self.client_socket
        self.server_key_2 = self.client_key
        self.server_socket_2.bind((tcp_ip, tcp_port))

   def start_to_listen(self):
        self.server_socket_2.listen(1)

   def send_message_to_client(self,msg,client_name):
        self.connection_socket_list_2[client_name].send(msg)

   def send_dict_message_to_client(self,msg,client_name):
        as_json_msg = json.dumps(msg)
        self.connection_socket_list_2[client_name].send(as_json_msg)

   def recv_message_from_client(self,client_name):
        return self.connection_socket_list_2[client_name].recv(BUFFER_SIZE)

   def accept_connection(self,client_name):
        temp_connection_socket , temp_client_addr = self.server_socket_2.accept()
        self.connection_socket_list_2[client_name] = temp_connection_socket
        self.client_addr_list_2[client_name] = temp_client_addr

   def close_server_connection(self,client_name):
        self.connection_socket_list_2[client_name].close()

   def get_peer_key(self):
        f = open( self.peer_name +'key.pem','r')
        self.peer_key = RSA.importKey(f.read())
        f.close()

   def run(self):

      if(self.context == 'client'):
        self.lock.acquire()
        if(self.client_name == 'alice'):
           print(Fore.RED + 'Step 1: \n\n')
        else:
           print(Fore.RED + 'Step 3: \n\n')
        print('Connecting from '+ self.client_name + ' to server')
        self.lock.release()
        self.connect_to_port((TCP_IP,TCP_SERVER_PORT))
        #print(self.client_name + ' requesting ' + self.peer_name + '\'s public key')
        print(Fore.WHITE + self.client_name + ' -> Server: Requesting ' + self.peer_name + '\'s public key ')
        self.send_message_to_server('get_client_address:'+ self.peer_name )
        #encrypt_msg = client.encrypt_for_server(client.get_hello_message())
        #client.send_message_to_server(encrypt_msg)
        jmsg_txt_encrypt = self.recv_message_from_server()
        #jmsg_txt = crypto.rsa_decrypt(jmsg_txt_encrypt, self.server_key)
        jmsg_txt = self.server_key.decrypt(jmsg_txt_encrypt)
        jmsg = json.loads(jmsg_txt)
        self.peer_key = jmsg['key']
        print(Fore.WHITE + self.peer_name + '\'s public key fingerprint:' +  self.peer_key)
        self.get_peer_key()
        print(Fore.WHITE + self.peer_name + '\'s public key :' +  self.peer_key.exportKey())
        #print(crypto.load_key_file('bobkey.pem').exportKey('PEM'))
        self.close_client_connection()
        
      if(self.context == 'peer1'):
        self.lock.acquire() 
        self.get_peer_key()
        #print(self.client_name + ' has started and ready for connection as peer\n')                
        self.connect_to_port((TCP_IP,TCP_PEER_PORT))
        self.lock.release()

        self.lock.acquire()
        print(Fore.RED + 'Step 5: \n\n')
        print(Fore.WHITE + self.client_name + ' sending ' + 'the nuance to ' + self.peer_name)
        self.client_guid = crypto.random_guid()
        jmsg1 = {"NA": self.client_guid,
                         "A": self.client_key_fprint}
        jmsg1_txt = json.dumps(jmsg1)
        print(Fore.WHITE + self.client_name + " ->" + self.peer_name + ": " + jmsg1_txt)
        jmsg1_txt_encrypt = self.peer_key.encrypt(jmsg1_txt,1)
        self.send_message_to_server(jmsg1_txt_encrypt[0])
        self.lock.release()


        jmsg2_txt_encrypt = self.recv_message_from_server()
        self.lock.acquire()
        jmsg2_txt = self.client_key.decrypt(jmsg2_txt_encrypt)
        jmsg2 = json.loads(jmsg2_txt)
        NA = jmsg2['NA']
        NB = jmsg2['NB']
        print(Fore.WHITE + self.client_name + 'got the message' +  jmsg2_txt)


        print(Fore.RED + 'Step 7: \n\n')
        print(Fore.WHITE + self.client_name + ' sending ' + 'the nuance back to ' + self.peer_name)
        jmsg3 = {'NB':NB}
        jmsg3_txt = json.dumps(jmsg3)
        print(Fore.WHITE + self.client_name + " ->" + self.peer_name + ": " + jmsg3_txt)
        jmsg3_txt_encrypt = self.peer_key.encrypt(jmsg3_txt,1)
        self.send_message_to_server(jmsg3_txt_encrypt[0])
        self.lock.release()
        #print(crypto.load_key_file('bobkey.pem').exportKey('PEM'))
        #print(Fore.WHITE + "Final message sent by "+ self.client_name)
        self.close_client_connection()
        

      if(self.context == 'peer2'): 
        self.lock.acquire() 
        self.get_peer_key()
        #print(self.client_name + ' has started and ready for connection as peer') 
        self.bind_to_port((TCP_IP,TCP_PEER_PORT))
        self.start_to_listen()
        self.lock.release()

        self.accept_connection(self.peer_name)      
        #print ('Connection address:', self.client_addr_list_2[self.peer_name])
        
        jmsg1_txt_encrypt = self.recv_message_from_client(self.peer_name)
        self.lock.acquire()
        jmsg1_txt = self.client_key.decrypt(jmsg1_txt_encrypt)
        jmsg1 = json.loads(jmsg1_txt)
        #print(jmsg1_txt)
        NA = jmsg1['NA']
        A =  jmsg1['A']
        
   
        #print('here is the client id' + clientid + '\\n')
        print(Fore.RED +'Step 6: \n\n')
        print(Fore.WHITE + self.client_name + ' sending ' + 'the nuance to' + self.peer_name)
        self.client_guid = crypto.random_guid()
        NB = self.client_guid     
        jmsg2 = {"NA":NA,"NB":NB} 
        jmsg2_txt = json.dumps(jmsg2)
        print(Fore.WHITE + self.client_name + " ->" + self.peer_name + ": " + jmsg2_txt)
        jmsg2_txt_encrypt = self.peer_key.encrypt(jmsg2_txt,1)                                           
        self.send_message_to_client(jmsg2_txt_encrypt[0],self.peer_name)
        self.lock.release()
        

        jmsg3_txt_encrypt = self.recv_message_from_client(self.peer_name)
        #print(msg3)
        jmsg3_txt = self.client_key.decrypt(jmsg3_txt_encrypt)
        jmsg3 = json.loads(jmsg3_txt)
        Nonce_peer = jmsg3['NB']
        #print(Fore.WHITE + "Final message received by "+ self.client_name + ":" + jmsg3_txt)
        self.close_server_connection(self.peer_name)

