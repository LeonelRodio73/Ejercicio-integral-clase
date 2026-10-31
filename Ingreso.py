import json
import re
import random

def ingresar_sueldo():
    sueldo = float(input("Ingrese el sueldo del vendedor: "))
    while sueldo < 0:
        print("El sueldo no puede ser negativo")
        sueldo = float(input("Ingrese el sueldo del vendedor: "))
    return sueldo

def ingresar_ventas():
    ventas = {}
    mes = str(input("Mes de la venta, -1 para finalizar: "))     
    while mes != "-1":
        venta = int(input("ingrese la cantidad de ventas del mes: "))
        while venta < 0:
            print("La cantidad de ventas no puede ser negativa")
            venta = int(input("ingrese la cantidad de ventas del mes: "))
        if mes in ventas:
            opcion = str(input('El mes que ingreso ya existe, ingrese "1" para reemplazarlo o ingrese "2" para sumarlo: '))
            while opcion != "1" and opcion != "2":
                print("Opción inválida")
                opcion = str(input('Ingrese "1" para reemplazarlo o "2" para sumarlo: '))
            if opcion == "1":
                ventas[mes] = venta
            else:
                ventas[mes] += venta
        else:
            ventas[mes] = venta
        mes = str(input("Mes de la venta, -1 para finalizar: "))
    return ventas

def guardar_archivo(diccionario):
    '''Guarda un diccionario en un archivo JSON.'''
    with open("Ventas.json", "w", encoding="utf-8") as f:
        json.dump(diccionario, f, ensure_ascii=False, indent=4)

def ingresar_legajo(legajo):
    '''Ingresa el legajo del vendedor, el sueldo y la cantidad de ventas del mismo.'''
    dic = {}
    dic[legajo] = {}
    dic[legajo]["sueldo"] = ingresar_sueldo()
    dic[legajo]["ventas"] = ingresar_ventas()
    guardar_archivo(dic)
    return dic
