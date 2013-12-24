from Crypto.PublicKey import RSA
msg = 'get_client_address:bob'
msg_list = msg.split(':')
print(msg_list[0],'ppp',msg_list[1])

key = RSA.generate(2048)
f = open('mykey.pem','w')
f.write(key.exportKey('PEM'))
f.close()

f = open('mykey.pem','r')
key = RSA.importKey(f.read())
private_key = key.exportKey()
public_key = key.publickey().exportKey()

ciphertext = key.encrypt('My name is mrinal', 1)
text = key.decrypt(ciphertext)
print(text)
