#método choice y se elige una palabra al azar dentro de un lista
from random import *

palabra=["azul","rojo","verde","amarillo"]
# función para elegir palabra aleatoria
def palabra_aleatoria(lista):
    return choice(lista)
print(palabra_aleatoria(palabra))

#función para hacer la palabra oculta
def palabra_oculta(palabra_aleatoria):
    oculta=["_"]*len(palabra)
    return oculta
print(palabra_oculta(palabra_aleatoria(palabra)))

"""
ya tengo la palabra aleatoria y los guiones de la  oculta.
necesito los intentos, las letras que están permitidas y las letras descartadas.
las letras descartadas las pondré en una lista que irá aumentando conforme falle.
"""
intentos=6
palabras_permitidas=list('abcdefghijklmnñopqrstuvwxyz')
palabras_descartadas=[]

#vamos a pedir la letra al usuario
def validar_letra(letra):
    if len(letra) != 1:
        print("has introducido más de una letra")
        return False
    elif letra not in palabras_permitidas:
        print("letra no valida, elige una correcta")
        return False
    elif letra in palabra_oculta():
        print("la letra ya está elejida")
    else:
        return True







