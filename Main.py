import json
import re
import random
import Ingreso as ingreso

def menu():
    print("1. Agregar vendedor\n2. Agregar ventas a un vendedor\n3. Modificar vendedor\n4. Modificar ventas de un vendedor\n5. Eliminar vendedor\n6. Eliminar venta de un vendedor")
    opcion = input("Ingrese una opción: ")
    while opcion not in ['1', '2', '3', '4', '5', '6']:
        opcion = input("Opción inválida. Ingrese una opción válida: ")
    if opcion == '1':
        ingreso.ingresar_legajo()
    elif opcion == '2':
        ingreso.buscar_vendedor()
    elif opcion == '3':
        ingreso.modificar_vendedor()
    elif opcion == '4':
        ingreso.ingresar_ventas()
    elif opcion == '5':
        ingreso.eliminar_vendedor()
    elif opcion == '6':
        ingreso.eliminar_venta()
 
 
with open("Ventas.json", "w", encoding="utf-8") as archivo:
    dic_ventas = ingreso.ingresar_legajo()
    json.dump(dic_ventas, archivo)
 
    





