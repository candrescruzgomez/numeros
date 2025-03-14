from datetime import datetime

# Solicitar al usuario que ingrese su año de nacimiento
ano_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))

# Obtener el año actual
ano_actual = datetime.now().year

# Calcular la edad
edad = ano_actual - ano_nacimiento

# Mostrar la edad calculada
print(f"Tu edad es: {edad} años")