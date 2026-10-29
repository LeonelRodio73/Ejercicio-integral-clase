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
    pase = str(input("Mes de la venta, -1 para finalizar: "))     
    while pase != "-1":
        venta = float(input("ingrese la cantidad de ventas del mes: "))
        while venta < 0:
            print("La cantidad de ventas no puede ser negativa")
            venta = float(input("ingrese la cantidad de ventas del mes: "))
        ventas[pase] = venta
        pase = str(input("Mes de la venta, -1 para finalizar: "))
    return ventas

def ingresar_legajo():
    dic = {}
    legajo = int(input("Ingrese el legajo del vendedor, ingrese -1 para finalizar: "))
    while legajo != -1:
        while legajo < 0:
            print("El legajo no puede ser negativo")
            legajo = int(input("Ingrese el legajo del vendedor, ingrese -1 para finalizar: "))
        if legajo != -1:
            dic[legajo] = {}
            dic[legajo]["sueldo"] = ingresar_sueldo()
            dic[legajo]["ventas"] = ingresar_ventas()
        legajo = int(input("Ingrese el legajo de otro vendedor, ingrese -1 para finalizar: "))
    return dic

with open("Ventas.json", "w", encoding="utf-8") as archivo:
    dic_ventas = ingresar_legajo()
    print(dic_ventas)
    json.dump(dic_ventas, archivo)