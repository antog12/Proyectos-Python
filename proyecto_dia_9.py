"""import shutil
shutil.unpack_archive("Proyecto+Dia+9.zip","Carpeta Proyecto dia 9","zip")"""

import re
import os
import time
import datetime
import pathlib
import math

inicio = time.time()

ruta = "C:\\Users\\A.Angel\\Desktop\\Formación\\Python Total-Programador avanzado en 16 días\\Python\\Día 9\\Carpeta Proyecto dia 9\\Mi_Gran_Directorio"

patron = r"N\D{3}-\d{5}" # patron para buscar

hoy = datetime.date.today() # día en el que estoy

nros_econtrados = []
archivos_encontrados = []

def buscar_numero(archivo,patron):
    este_archivo = open(archivo,"r")
    texto = este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ""

def crear_listas():
    for carpeta,subcarpeta,archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(pathlib.Path(carpeta, a), patron)
            if resultado != "":
                nros_econtrados.append(resultado.group())
                archivos_encontrados.append(a.title())




def mostrar_todo():
    indice = 0
    print("-"*50)
    print(f"Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("ARCHIVO\t\t\tNRO.SERIE")
    print("-------\t\t\t-------")
    for a in archivos_encontrados:
        print(f"{a}\t{nros_econtrados[indice]}")
        indice = indice + 1
    print("\n")
    print(f"número encontrados: {len(nros_econtrados)}")
    fin = time.time()
    duracion = fin-inicio
    print(f"Duración de la busqueda: {math.ceil(duracion)} segundos")
    print("-" * 50)


crear_listas()
mostrar_todo()

























