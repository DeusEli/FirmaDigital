from Crypto import Random
from Crypto.PublicKey import RSA

random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)

privateKey = rsa.exportKey()
with open('PrivateKey.txt', 'wb') as f:
	f.write(privateKey)
	f.close()
 
publicKey = rsa.publickey().exportKey()
with open('PublicKey.txt', 'wb') as f:
	f.write(publicKey)
	f.close()

print("Se generó la clave privada y se guardó en el archivo PrivateKey.txt")
print("Se generó la clave pública y se guardó en el archivo PublicKey.txt") 
