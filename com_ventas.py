import json
import re
import random

def menu():
    print("1. Agregar vendedor")
    print("2. Agregar ventas a un vendedor")
    print("3. Modificar vendedor")
    print("4. Modificar ventas de un vendedor")
    print("5. Eliminar vendedor")
    print("6. Eliminar venta de un vendedor")
    opcion = input("Ingrese una opción: ")
    while opcion not in ['1', '2', '3', '4', '5', '6']:
        opcion = input("Opción inválida. Ingrese una opción válida: ")
    if opcion == '1':
        ingresar_legajo()
    elif opcion == '2':
        buscar_vendedor()
    elif opcion == '3':
        modificar_vendedor()
    elif opcion == '4':
        ingresar_ventas()
    elif opcion == '5':
        eliminar_vendedor()
    elif opcion == '6':
        eliminar_venta()
 
def ingresar_sueldo():
    sueldo = float(input("Ingrese el sueldo del vendedor: "))
    while sueldo < 0:
        print("El sueldo no puede ser negativo")
        sueldo = float(input("Ingrese el sueldo del vendedor: "))
    return sueldo
 
def ingresar_ventas():
    ventas = []
    pase = str(input("Quieres ingresar ventas? (s/n): "))    
    while pase != "n":
        venta = float(input("Ingrese el monto de la venta: "))
        while venta < 0:
            print("El monto de la venta no puede ser negativo")
            venta = float(input("Ingrese el monto de la venta: "))
            ventas.append(venta)
        pase = str(input("Quiere ingresar otra venta? (s/n): "))
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
    json.dump(dic_ventas, archivo)
 
    






