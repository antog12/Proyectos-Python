from random import *

nombre = input("dime tu nombre: ")
print(f"Bueno, {nombre}, he pensado un número entre el 1 y el 100\ny tienes sólo 8 intentos para adivinar el número")
print("--------")

intentos = 8
aleatorio = randint(1, 101)
respuesta_correcta = aleatorio

while intentos > 0:
    num = int(input("Di un número: "))
    if num < 1 or num > 100:
        print("Ese número no está permitido")
    elif num < aleatorio:
        print("respuesta incorrecta. El número elegido es más alto")
    elif num > aleatorio:
        print("respuesta incorrecta. El número elegido es más bajo")
    elif num == aleatorio:
        print("acertaste el número secreto", respuesta_correcta)
        break
    intentos = intentos - 1
    print("número de intentos", intentos)
else:
    print(f"Te has quedado sin intentos, el número secreto era {respuesta_correcta}")
