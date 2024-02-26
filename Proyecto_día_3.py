ingresa_texto=input("Ingresa un texto: ")
texto_min=ingresa_texto.lower()
print(texto_min)
print("----------")
letra1= input(" ingresa una letra:")
letra2= input(" ingresa otra letra:")
letra3= input(" ingresa una última letra:")

print(letra1)
print(letra2)
print(letra3)

print("----------")
print("---Análisis 1---")
print("----------")

x=texto_min.count(letra1)
y=texto_min.count(letra2)
z=texto_min.count(letra3)

print(f"la letra '{letra1}', aparece {x} veces,la letra '{letra2}', aparece dos veces {y} y la\nla letra '{letra3}', aparece {z} veces.")

print("----------")
print("---Análisis 2---")
print("----------")

print("Cuántas palabras hay en el texto?")
palabra=texto_min.split() # me crea una lista de palabras
print(f"En el texto hay {len(palabra)} palabras")

print("----------")
print("---Análisis 3---")
print("----------")

print("Cuál es la primera letra del texto?")
primera=texto_min[0]
print(f" La letra inicial es '{primera}'")
print("Cuál es la última letra del texto?")
ultima=texto_min[-2] # pongo -2 pq -1 es un espacio
print(f" La letra final  es '{ultima}'")

print("----------")
print("---Análisis 4---")
print("----------")

lista=texto_min.split()
print(lista)
lista_invertida= lista[::-1]
print(lista_invertida)
unir_invertida=" ".join(lista_invertida)
print(f"El texto invertido es: '{unir_invertida}'")

print("----------")
print("---Análisis 5---")
print("----------")

dic={"valor":texto_min}
control="Python" in dic
print(f"La respuesta es: '{control}'.")






