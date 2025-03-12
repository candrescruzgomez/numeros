def es_primo(n):
    """
    Función para verificar si un número es primo.
    Un número es primo si solo es divisible por 1 y por sí mismo.
    """
    if n < 2:
        return False  # Los números menores que 2 no son primos
    for i in range(2, int(n**0.5) + 1):  # Verificar divisores hasta la raíz cuadrada de n
        if n % i == 0:
            return False  # Si tiene un divisor, no es primo
    return True  # Si no tiene divisores, es primo

def es_compuesto(n):
    """
    Función para verificar si un número es compuesto.
    Un número es compuesto si no es primo y es mayor que 1.
    """
    return n > 1 and not es_primo(n)

# Programa principal
def main():
    print("Verificar si los números ingresados son compuestos")
    try:
        # Pedir al usuario que ingrese números separados por comas
        entrada = input("Ingresa los números separados por comas (ejemplo: 4, 6, 7, 10): ")
        
        # Convertir la entrada en una lista de números enteros
        numeros = [int(numero.strip()) for numero in entrada.split(",")]
        
        print("\nResultados:")
        for numero in numeros:
            if es_compuesto(numero):
                print(f"El número {numero} **es compuesto**.")
            else:
                print(f"El número {numero} **no es compuesto** (es primo o menor que 2).")
    except ValueError:
        print("¡Error! Asegúrate de ingresar números válidos separados por comas.")

# Ejecutar el programa
main()