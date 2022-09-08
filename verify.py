from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5
import base64

def verify(msg, firm):
	with open('PublicKey.txt') as f:
		key=f.read()
		rsakey=RSA.importKey(key)
		signer=Signature_PKCS1_v1_5.new(rsakey)
		digest=SHA.new()
		digest.update(msg)
  
		print("Calculando el HASH del documento: ", digest.hexdigest())
		print("Verificando la firma: ", firm)
  
		is_verify=signer.verify(digest, base64.b64decode(firm))
  
		if is_verify:
			print("La firma es válida")
			print("El documento no ha sido modificado")
			print("El documento es auténtico")
		else:
			print("La firma no es válida")
			print("El documento ha sido modificado")
			print("El documento no es auténtico")

with open ('Documento.txt') as f:
	msg=f.read()
	f.close()

with open ('Signature.txt') as f:
	firm=f.read()
	f.close()

msg=msg.encode()
verify(msg, firm)