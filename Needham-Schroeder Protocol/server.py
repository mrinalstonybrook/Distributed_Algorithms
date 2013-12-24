#!/usr/bin/env python

import socket
import server_new
from Crypto.PublicKey import RSA

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

def server_start():

 server_key = RSA.generate(2048)
 f = open('serverkey.pem','w')
 f.write(server_key.publickey().exportKey('PEM'))
 f.close()

 server = server_new.Server_proto(server_key)
 server.bind_to_port((TCP_IP, TCP_PORT))
 
 print('Connection to Alice')
 
 server.start_to_listen()
 server.accept_connection('alice')
 server.load_client_keys()

 print ('Connection address:', server.client_addr_list['alice'])
 while 1:
     msg = server.recv_message_from_client('alice')
     if not msg: break
     msg_list = msg.split(':')
     if(msg_list[0] == 'get_client_address'):
         server.send_public_key(msg_list[1],'alice')
 server.close_connection('alice')

 print('Connecting to Bob')

 #server.start_to_listen()
 server.accept_connection('bob')
 #server.load_client_keys()

 print ('Connection address:', server.client_addr_list['bob'])
 while 1:
     msg = server.recv_message_from_client('bob')
     if not msg: break
     msg_list = msg.split(':')
     if(msg_list[0] == 'get_client_address'):
         server.send_public_key(msg_list[1],'bob')
 server.close_connection('bob')
 


print('Starting the server\n')
server_start()

#conn, addr = s.accept()
#print ('Connection address:', addr)
#while 1:
#    data = conn.recv(BUFFER_SIZE)
#    if not data: break
#    print ("received data:", data)
#    conn.send("received the message")  # echo
#conn.close()
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
#s.listen(1)

#conn, addr = s.accept()
#print ('Connection address:', addr)
#while 1:
#    data = conn.recv(BUFFER_SIZE)
#    if not data: break
#    print ("received data:", data)
#    conn.send("received the message")  # echo
#conn.close()
    
    
