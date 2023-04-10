

from os import system as interfaz
from sys import path as ruta
ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL")
import BD.Servicios as BDs

try:
    while True:
        interfaz("cls")
        opcion=int(input("Bienvenido al menu \nOprima 1 si desea manejar los servicios \nOprima 2 si desea salir del programa \n"))
        match opcion:
            case 1:
                while True:
                    interfaz("cls")
                    opcionS=int(input("Oprima 1 si desea agregar los precios de servicios usados a un cliente \nOprima 2 si desea cambiar algun dato de los servicios usados de un cliente \nOprima 3 si desea consultar todos los datos de la tabla \nOprima 4 si desea eliminar el registro de los servicios de un cliente \nOprima 5 para volver al menu principal \n"))
                    match opcionS:
                        case 1:
                            BDs.create()
                        case 2:
                            BDs.update()
                        case 3:
                            BDs.read()
                        case 4:
                            BDs.delete()
                        case 5:
                            break
                        case _:
                            print("El numero no es valido")
                    interfaz("pause")
            case 2:
                break
            case _:
                print("El numero no es valido")
        interfaz("pause")
        print("Escoja un numero valido")
except (TypeError, ValueError) as e:
    print(type(e),e)