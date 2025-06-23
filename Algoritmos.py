# Paso 1 : Solicitar al usuario que ingrese el radio del circulo.

import math

radio = float(input("Por favor, ingrese el radio del circulo: "))

# Paso 2: Calcular el area del circulo utilizando la formula area = π * radio^2

area = math.pi * (radio**2) # π * radio^2

# Paso 3: Mostrar al usuario el area calculada

print("El area del circulo con radio", radio, "es:", area)
