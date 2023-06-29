import time
from funciones import *

menu = True
tipo, patente, marca, precio, fecha_multa, monto_multa,fecha_registro, nombre_dueno = 0,0,0,0,0,0,0,0
autos = []

while menu == True:
    try:
        lista_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1": #Grabar
            tipo = input("Ingrese tipo del vehiculo: ")
            patente = input("Ingrese Patente del vehiculo: ")
            marca = input("Ingrese Marca del vehiculo: ")
            precio = int(input("Ingrese Precio del vehiculo: "))
            fecha_multa = input("Ingrese fecha de multa del vehiculo: ")
            monto_multa = input("Ingrese Monto de multa del vehiculo: ")
            fecha_registro = input("Ingrese Fecha registro: ")
            nombre_dueno = input("Ingrese Nombre Dueño del vehiculo: ")
            if validacion_auto(patente,marca,precio) == True:
                auto = (tipo, patente, marca, precio, fecha_multa, monto_multa,fecha_registro, nombre_dueno)
                autos.append(auto)
                print(autos)
            else:
                print("Datos no validos.")
        elif opcion == "2": #Buscar
            busqueda_auto(autos,patente)
        elif opcion == "3": #Imprimir
            print(busqueda_auto)
        elif opcion == "4": #Salir
            print("Usted ha salido del programa gracias por utilizarlo.")
            print("Rodrigo Concha")
            print("Version 1.0.0")
            menu = False
    except:
        print("Ocurrió un error. Por favor, intente nueva1mente.")