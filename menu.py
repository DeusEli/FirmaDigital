from createKey import CreateKeys
from firmaDigital import CreateFirm

option = 0

while option != 4:
	print("Menú")
	print("1. Crear llaves")
	print("2. Escribir y firmar documento")
	print("3. verificar documento")
	print("4. Salir")
	option = int(input("Ingrese una opción: "))
	if option == 1:
		print("\n")
		print("Opción 1 seleccionada")
		CreateKeys()
	elif option == 2:
		print("\n")
		print("Opción 2 seleccionada")
		CreateFirm()
	elif option == 3:
		print("\n")
		print("Opción 3")
	elif option == 4:
		print("\n")
		print("Adiós")
	else:
		print("Opción no válida")