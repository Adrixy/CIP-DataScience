edad = int(input("Digite su edad: "))
nombre = input("Ingresa tu nombre: ")
letra = nombre[0].upper()
vocales = "AEIOU"

if edad < 18 and letra in vocales:
    print("Pertenece al grupo 1")
elif edad >= 18 and letra not in vocales:
    print("Pertenece al grupo 2")
else:
    print("Pertenece al grupo 3")
