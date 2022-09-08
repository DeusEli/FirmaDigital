from Crypto import Random
from Crypto.PublicKey import RSA

def CreateKeys():
	random_generator = Random.new().read
	rsa = RSA.generate(1024, random_generator)
	privateKey = rsa.export_key()
	with open('PrivateKey.txt', 'wb') as f:
		f.write(privateKey)
		f.close()
	
	publicKey = rsa.publickey().export_key()
	with open('PublicKey.txt', 'wb') as f:
		f.write(publicKey)
		f.close()
	
	print("\n")
	print("Se generaron las llaves pública y privada")
	print("Se guardó la llave pública en el archivo PublicKey.txt")
	print("Se guardó la llave privada en el archivo PrivateKey.txt")
	print("\n")
