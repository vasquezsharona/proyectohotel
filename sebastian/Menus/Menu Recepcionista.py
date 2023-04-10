
from os import system as interfaz
from sys import path as ruta
ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL")
import BD.Reserva as BDr

try:
    while True:
        interfaz("cls")
        opcion=int(input("Bienvenido al menu \nOprima 1 si desea manejar las reservas \nOprima 2 para salir del programa \n"))
        match opcion:
            case 1:
                while True:
                    interfaz("cls")
                    opcionR=int(input("Oprima 1 si desea agregar una reserva desde 0 \nOprima 2 si desea actualizar los datos de alguna reserva \nOprima 3 si desea consultar los datos de toda la tabla \nOprima 4 si desea eliminar una reserva ya creada anteriormente \nOprima 5 para volver al menu principal \n"))
                    match opcionR:
                        case 1:
                            BDr.create()
                        case 2:
                            BDr.update()
                        case 3:
                            BDr.read()
                        case 4:
                            BDr.delete()
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