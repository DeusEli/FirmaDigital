import base64
from inspect import signature
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5

def firm(msg):
    with open('PrivateKey.txt') as f:
        key=f.read()
        rsakey=RSA.importKey(key)
        signer=Signature_PKCS1_v1_5.new(rsakey)
        
        digest=SHA.new()
        
        digest.update(msg)
        print("\n")
        print("Contenido del documento: ", msg)
        print("Se generó el HASH: ", digest.hexdigest())
        print("\n")
        
        sign=signer.sign(digest)
        
        signature=base64.b64encode(sign)
        print("Se generó la firma: ", signature)
        f.close()
    
    with open('Signature.txt', 'wb') as f:
        f.write(signature)
        f.close()
        
    print("Se guardó la firma en el archivo Signature.txt")
    print("\n")
    return signature

def CreateFirm():
    print("\n")
    documentData = input("Ingrese el contenido del documento a firmar: ")
    with open('Documento.txt', 'w') as f:
        f.write(documentData)
        f.close()
        
    with open('Documento.txt') as f:
        msg=f.read()
        f.close()
        
    msg=msg.encode()
    firm(msg)
