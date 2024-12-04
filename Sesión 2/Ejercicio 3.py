puntuacion = float(input("Ingrese la puntuación de tu proyecto: "))

if puntuacion == 1.0:
    nivel = "Bajo"
elif puntuacion == 1.5:
    nivel = "Medio"
elif puntuacion == 2.0:
    nivel = "Alto"
elif puntuacion >= 2.5:
    nivel = "Excelente"
else:
    print("Puntuación no valida")
    sys.exit()

if nivel:
    bono = puntuacion * 3000000
    print(f"Nivel de rendimiento: {nivel}")
    print(f"Bono: {bono:,} pesos")
