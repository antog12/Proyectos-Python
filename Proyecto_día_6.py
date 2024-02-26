from pathlib import Path
import os

print("----------")
print("RECETARIO")
print("----------")

nombre = input("Tu nombre: ")
ruta = Path("C:/Users/A.Angel/Desktop/Formación/Python Total-Programador avanzado en 16 días/Apuntes día 6/Recetas")

print("*************")
print("*************")

print(f"Bienvenido {nombre} de nuevo al recetario.\nLa ruta del directorio de recetas es: {ruta}.\n")
print("Las recetas son:")

cuenta = 0
for txt in ruta.glob("**/*.txt"):
    print(txt.name)
    cuenta = cuenta + 1
print(f"El número total de archivos es: {cuenta}")

print("*************")
print("METADATOS")
print("*************")

metadata = ruta.stat()
print(metadata)

print("----------------------------------------------------")

print("----------------------------------------------------")

print("----------------------------------------------------")


def recetario():
    menu = "x"
    while not menu.isnumeric() or int(menu) not in range(1, 7):
        print("Elija uno de los siguientes menus: ")
        print("""
        [1] - Elegir carpeta y leer archivo.
        [2] - Elegir carpeta y crear nueva receta.
        [3] - Crear nueva categoría.
        [4] - Eliminar receta.
        [5] - Eliminar categoría.
        [6] - Salir del programa
        """)
        menu = input()
        match menu:
            case "1":
                leer_archivo()

            case "2":
                crear_archivo()

            case "3":
                crear_categoria()

            case "4":
                eliminar_archivo()

            case "5":
                eliminar_categoria()

            case "6":
                print("salir del programa")
                break


def leer_archivo():
    ruta = Path("C:/Users/A.Angel/Desktop/Formación/Python Total-Programador avanzado en 16 días/Apuntes día 6/Recetas")
    print("***************")
    print("**Directorios**")
    print("***************")
    for directorio in ruta.iterdir():
        if directorio.is_dir():
            print(directorio.name)
    ruta_directorio = input("Qué directorio quieres abrir?")
    nombre_archivo = input("Que archivo quieres abrir?")
    ruta_relativa = ruta / ruta_directorio
    ruta_completa = os.path.join(ruta_relativa, nombre_archivo)
    archivo = open(ruta_completa, "r")
    print(archivo.read())


# print(menu1(ruta_directorio=Path(input()), nombre_archivo=Path(input())))


def crear_archivo():
    ruta = Path("C:/Users/A.Angel/Desktop/Formación/Python Total-Programador avanzado en 16 días/Apuntes día 6/Recetas")
    print("***************")
    print("**Directorios**")
    print("***************")
    for directorio in ruta.iterdir():
        if directorio.is_dir():
            print(directorio.name)
    ruta_directorio = input("Qué directorio quieres abrir?")
    nombre_archivo = input("Nombre de archivo a crear?")
    ruta_relativa = ruta / ruta_directorio
    ruta_completa = os.path.join(ruta_relativa, nombre_archivo)
    archivo = open(ruta_completa, "x")
    archivo.close()
    print("archivo creado")

    if os.path.isfile(ruta_completa):
        archivo = open(ruta_completa, "w")
        archivo.write("receta de chuleton")
        archivo.close()

    else:
        print("el archivo no existe.")


# print(menu2(ruta_directorio=Path(input()), nombre_archivo=Path(input())))

def crear_categoria():
    ruta = Path("C:/Users/A.Angel/Desktop/Formación/Python Total-Programador avanzado en 16 días/Apuntes día 6/Recetas")
    directorio = input("Nombre del directorio a crear: ")
    ruta_completa = ruta / directorio
    ruta_completa.mkdir()
    print("Categoría creada")
    return ruta_completa


def eliminar_archivo():
    ruta = Path("C:/Users/A.Angel/Desktop/Formación/Python Total-Programador avanzado en 16 días/Apuntes día 6/Recetas")
    print("***************")
    print("**Directorios**")
    print("***************")
    for directorio in ruta.iterdir():
        if directorio.is_dir():
            print(directorio.name)
    ruta_directorio = input("Qué directorio quieres abrir?")
    nombre_archivo = input("Que archivo quieres eliminar?")
    ruta_relativa = ruta / ruta_directorio
    ruta_completa = os.path.join(ruta_relativa, nombre_archivo)
    eliminar = os.remove(ruta_completa)
    print("archivo eliminado")
    return eliminar


def eliminar_categoria():
    ruta = Path("C:/Users/A.Angel/Desktop/Formación/Python Total-Programador avanzado en 16 días/Apuntes día 6/Recetas")
    directorio = input("Nombre del directorio a eliminar: ")
    ruta_completa = ruta / directorio
    ruta_completa.rmdir()
    print("Categoría eliminada")
    return ruta_completa


recetario()
