# Definir un arreglo (lista) de números
arreglo = [1, 2, 3, 4, 5]

# Inicializar la suma de cuadrados
suma_cuadrados = 0

# Calcular la suma de cuadrados
for numero in arreglo:
    suma_cuadrados += numero**2  # Elevar al cuadrado y sumar

# Mostrar el resultado
print("La suma de cuadrados es:", suma_cuadrados)