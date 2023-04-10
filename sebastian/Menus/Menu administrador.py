
from os import system as interfaz
from sys import path as ruta
ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL")
import BD.Habitacion as BDh
import BD.Mesero as BDm
import BD.Administrador as BDa

try:
    while True:
        interfaz("cls")
        print("Bienvenido al menu \nPresione 1 para editar los datos de las habitaciones \nPresione 2 para editar los datos del mesero \nPresione 3 si desea editar los datos de administrador \nPresione 4 para finalizar el programa")
        pedir=int(input(''))
        match pedir:
            case 1:
                while True:
                    interfaz("cls")
                    opcion=int(input("Oprima 1 si desea crear una nueva habitacion \nOprima 2 si desea actualizar los datos de una habitacion ya creada \nOprima 3 si desea consultar los datos de la tabla \nOprima 4 si desea eliminar una habitacion \nOprima 5 si desea volver al menu principal \n"))
                    match opcion:
                        case 1:
                            BDh.create()
                        case 2:
                            BDh.update()
                        case 3:
                            BDh.read()
                        case 4:
                            BDh.delete()
                        case 5:
                            break
                        case _:
                            print("El numero no es valido")
                    interfaz("pause")
            case 2:
                while True:
                    interfaz ("cls")
                    opcionM=int(input("Oprima 1 si desea agregar un nuevo mesero \nOprima 2 si desea actualizar los datos de un mesero ya agregado \nOprima 3 si desea consultar los datos de la tabla completa \nOprima 4 si desea remover un mesero de la tabla \nOpimra 5 si desea volver al menu principal \n"))
                    match opcionM:
                        case 1:
                            BDm.create()
                        case 2:
                            BDm.update()
                        case 3:
                            BDm.read()
                        case 4:
                            BDm.delete()
                        case 5:
                            break
                        case _:
                            print("El numero no es valido")
                    interfaz ("pause")
            case 3:
                while True:
                    interfaz ("cls")
                    opcionA=int(input("Oprima 1 si desea agregar un nuevo administrador \nOprima 2 si desea remover un administrador de la tabla \nOprima 3 si desea volver al menu principal \n"))
                    match opcionA:
                        case 1:
                            BDa.register()
                        case 2:
                            BDa.deleteAdmin()
                        case 3:
                            break
            case 4:
                break
            case _:
                print('El numero no es valido')
        interfaz("pause")
        print("Escoja un numero valido")
except (TypeError, ValueError) as e:
    print(type(e), e)