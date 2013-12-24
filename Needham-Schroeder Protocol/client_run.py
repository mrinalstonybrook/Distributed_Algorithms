#!/usr/bin/env python

import socket
import crypto
import client_new
import server_new
from Crypto.PublicKey import RSA
import threading
from colorama import Fore, Back, Style


TCP_IP = '127.0.0.1'
TCP_SERVER_PORT = 5005
TCP_PEER_PORT = 5006
MESSAGE = "Hello, World!"

# creation of keys for server and client
server_key = RSA.generate(2048)
f = open('serverkey.pem','w')
f.write(server_key.publickey().exportKey('PEM'))
f.close()

f = open('serverkey.pem','r')
server_key_public = RSA.importKey(f.read())
f.close()

client_key_alice = RSA.generate(2048)
f = open('alicekey.pem','w')
f.write(client_key_alice.publickey().exportKey('PEM'))
f.close()

client_key_bob = RSA.generate(2048)
f = open('bobkey.pem','w')
f.write(client_key_bob.publickey().exportKey('PEM'))
f.close()

# creating the server thread and obtaining lock for the same
threadLock = threading.Lock()
server = server_new.Server_proto(server_key,threadLock)
client_alice = client_new.Client_proto('alice','bob','client',client_key_alice,server_key,threadLock)
client_bob = client_new.Client_proto('bob','alice','client',client_key_bob,server_key,threadLock)

server.start()
client_alice.start()
client_alice.join()
client_bob.start()
client_bob.join()

#start of the peer-to-peer communication
print(Fore.WHITE + 'Start Bob as server and Alice as client')
threadLock = threading.Lock()
client_alice = client_new.Client_proto('alice','bob','peer1',client_key_alice,server_key,threadLock)
client_bob = client_new.Client_proto('bob','alice','peer2',client_key_bob,server_key,threadLock)
client_bob.start()
client_alice.start()

client_bob.join()
client_alice.join()
print(Fore.WHITE + '\n\n Done with communication')

