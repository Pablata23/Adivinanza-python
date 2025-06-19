# Juego de Adivinanza
    
import random


# numero_secreto = random.randint(1,100)
# cant_intentos = 0
# cant_max_intentos = 5
# adivinado = False

# print("Bienvenido al juego de la adivinanza!")

# while not adivinado and cant_intentos < cant_max_intentos:
#     entrada = input("Introduce un numero del 1 al 99: ") 
#     numero = int(entrada)

#     if numero == numero_secreto:
#         print("Felicidades, adivinaste el numero secreto!!")
#         adivinado = True
#     elif numero < numero_secreto:
#         print("Pista: el numero es mayor al ingresado")
#     else:
#         print("Pista: el numero es menor al ingresado")
    
#     cant_intentos += 1

# if not cant_intentos < cant_max_intentos:
#     print("GAME OVER!! No pudiste adivinar el numero")


#######
#######

# OTRA MANERA DE HACER LO ANTERIOR

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de la adivinanza!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("GAME OVER!! No pudiste adivinar el numero")
        break
    
    entrada = input("Introduce un numero del 1 al 99: ") 
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicidades, adivinaste el numero secreto!!")
        adivinado = True
    elif numero < numero_secreto:
        print("Pista: el numero es mayor al ingresado")
    else:
        print("Pista: el numero es menor al ingresado")
    
    cant_intentos += 1
