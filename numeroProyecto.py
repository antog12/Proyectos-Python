# tres generadores
def numeros_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1,10000):
        yield f"C - {n}"

# las envolvemos en variables
p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

# decorador para los 3 variables de clientela
def decorador(rubro):
    print("\n" + "*" * 23)
    print("su numero es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")










