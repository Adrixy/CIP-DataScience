pais = input("Ingresa tu país de origen: ")
nombre = input("Ingresa tu nombre: ")
longnombre = len(nombre)

if pais.lower() == "colombia" and longnombre < 5:
    print("Pertenece al grupo de Colombia A")
elif pais.lower() == "méxico" and longnombre >= 5:
    print("Pertenece al grupo de México B")
else:
    print("Pertenece al grupo de otros")
