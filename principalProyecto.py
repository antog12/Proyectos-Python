import numeros

def preguntar():
    print("Bienvenido a Farmacia Python")
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmetica ")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P","F","C"].index(mi_rubro) # arroja un error si lo que pone el user no está en esta línea
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)

#darle inicio al código

def main():
    while True:
        preguntar()
        try:
            otroturno = input("Quieres sacar otro turno? [S] [N]").upper()
            ["S","N"].index(otroturno) # si da error, nos manda a la excepción
        except ValueError:
            print("Esa no es una opción valida")
        else:
            if otroturno == "N":
                print("Gracias por su visita")
                break


main()


























