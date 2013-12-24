#!/usr/bin/env python

import socket
import crypto
import client_new
from Crypto.PublicKey import RSA


TCP_IP = '127.0.0.1'
TCP_SERVER_PORT = 5005
TCP_PEER_PORT = 5006
MESSAGE = "Hello, World!"

client_key_alice = RSA.generate(2048)
f = open('alicekey.pem','w')
f.write(client_key_alice.publickey().exportKey('PEM'))
f.close()

client_key_bob = RSA.generate(2048)
f = open('bobkey.pem','w')
f.write(client_key_bob.publickey().exportKey('PEM'))
f.close()

f = open('serverkey.pem','r')
key = RSA.importKey(f.read())
f.close()

print('Connecting from Alice to Server\n')
server_key = key
client_alice = client_new.Client_proto('alice',client_key_alice,server_key)
client_alice.connect_to_port((TCP_IP,TCP_SERVER_PORT))

print('Connecting from Bob to Server\n')
server_key = key
client_bob = client_new.Client_proto('bob',client_key_alice,server_key)
client_bob.connect_to_port((TCP_IP,TCP_SERVER_PORT))

print('Alice requesting Bob\'s public key')
client_alice.send_message_to_server('get_client_address:bob')
#encrypt_msg = client.encrypt_for_server(client.get_hello_message())
#client.send_message_to_server(encrypt_msg)
data = client_alice.recv_message_from_server()
print('Bob\'s public key:', data)
print(crypto.load_key_file('bobkey.pem').exportKey('PEM'))
client_alice.close_client_connection()

print('Bob requesting Alice\'s public key')
client_bob.send_message_to_server('get_client_address:alice')
#encrypt_msg = client.encrypt_for_server(client.get_hello_message())
#client.send_message_to_server(encrypt_msg)
data = client_bob.recv_message_from_server()
print('Alice\'s public key:', data)
print(crypto.load_key_file('alicekey.pem').exportKey('PEM'))
client_bob.close_client_connection()

#start Bob as server
print('Start Bob as server and Alice as client')
client_bob.bind_to_port((TCP_IP,TCP_PEER_PORT))
client_alice.connect_to_port((TCP_IP,TCP_PEER_PORT))


#TCP_IP = '127.0.0.1'
#TCP_PORT = 5005
#BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!"

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)
#data = s.recv(BUFFER_SIZE)
#s.close()

#print ("received data:", data)


