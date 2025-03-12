# Definir los arreglos (ejemplo con valores aleatorios)
import random

arreglo1 = [random.randint(1, 100) for _ in range(100)]
arreglo2 = [random.randint(1, 100) for _ in range(100)]

# Inicializar las sumas
suma_pares_arreglo1 = 0
suma_impares_arreglo2 = 0

# Sumar elementos en posiciones pares del primer arreglo
for i in range(0, 100, 2):
    suma_pares_arreglo1 += arreglo1[i]

# Sumar elementos en posiciones impares del segundo arreglo
for i in range(1, 100, 2):
    suma_impares_arreglo2 += arreglo2[i]

# Calcular la suma total
suma_total = suma_pares_arreglo1 + suma_impares_arreglo2

# Mostrar el resultado
print("La suma total es:", suma_total)