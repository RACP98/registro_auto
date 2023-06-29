import numpy as np

def lista_menu():
    print("“Menu Auto Seguro”")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificado")
    print("4. Salir")

def verificar_patente(patente):
    if len(patente) == 6:
        return True
    else:
        return False
    
def verificar_marca(marca):
    if len(marca) >= 2 and len(marca) <= 15:
        return True
    else:
        False
    
def verificar_precio(precio):
    if precio >= 5000000:
        return True
    else:
        return False
    
def validacion_auto(patente,marca,precio):
    if verificar_patente(patente) == True:
        if verificar_marca(marca) == True:
            if verificar_precio(precio)== True:
                return  True
    else:
        return False
    
def busqueda_auto(autos,patente):
    busqueda_patente = input("Ingrese la patente del vehiculo que desea buscar: ")
    for busqueda_patente in autos:
        if busqueda_patente == autos[1]:
            print(autos[busqueda_patente])
            