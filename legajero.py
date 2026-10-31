import json

def leer_archivo():
    '''Lee el contenido de un archivo JSON y lo devuelve como un diccionario.'''
    try:
        with open("legajos.json", "r", encoding="utf-8") as f:
            diccionario = json.load(f)
    except FileNotFoundError:
        print("El archivo legajos.json no existe.")
        return {}
    except json.JSONDecodeError:
        print("El archivo legajos.json no contiene JSON válido.")
        return {}
    return diccionario

def guardar_archivo(archivo, diccionario):
    '''Guarda un diccionario en un archivo JSON.'''
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(diccionario, f, ensure_ascii=False, indent=4)

def cargar_legajos(legajo):
    '''Pide los datos de un vendedor, lo agrega al diccionario y lo guarda en el archivo JSON.'''
    legajero = leer_archivo()
    print("Legajos cargados:", legajero)
    while legajo <0 or len(str(legajo)) < 3:
        legajo = int(input("Ingrese el legajo del vendedor (debe ser un número positivo con al menos 3 dígitos): "))
    while legajo in legajero:
        print("El legajo ya existe. Ingrese un legajo diferente.")
        legajo = int(input("Ingrese el legajo del vendedor: "))

    nombre = input("Ingrese el nombre del vendedor: ")#falta validar nombre con regex
    correo = input("Ingrese el correo del vendedor: ")#falta validar correo con regex

    legajero[legajo] = {"nombre": nombre, "correo": correo}
    guardar_archivo("legajos.json", legajero)
    return legajero