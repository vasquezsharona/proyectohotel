
from sqlite3 import *
from sys import path as ruta
from os import system as interfaz


ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez")
import Clases.Habitacion as CH


def create():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursorcreate=con.cursor()
    numero_habitacion=int(input("Ingrese el numero de la habitacion a agregar: "))
    tipo_habitacion=input("Ingrese el tipo de la habitacion a agregar: ")
    precio_habitacion=int(input("Ingrese el precio de la habitacion a agregar: "))
    estado_habitacion=input("Ingrese el estado de la habitacion: ")
    Habit=CH.Habitacion(numero_habitacion,tipo_habitacion,precio_habitacion,estado_habitacion)
    create=(Habit.getNum(),Habit.getTipo(),Habit.getPrecio(),Habit.getEstado())
    micursorcreate.execute("insert into Habitacion values(?,?,?,?)", create)
    con.commit()
    con.close()
    
    with open("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\\Reportes\\Reporte_habitacion.txt","a") as flujo:
        flujo.write("Numero de la habitacion: " + str(Habit.getNum()) + 
                    "\nTipo de habitacion: " + Habit.getTipo() + 
                    "\nPrecio de la habitacion: " + str(Habit.getPrecio()) + 
                    "\nEstado de la habitacion: " + Habit.getEstado() + 
                    "\n" + "*"*50 + 
                    "\n")



def update():
    while True:
        interfaz("cls")
        con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
        micursorupdate=con.cursor()
        print("¿Cual es la columna que desea actualizar? \nOprima 1 para editar una columna entera \nOprima 2 para editar el tipo de habitacion \nOprima 3 para editar el precio de habitacion \nOprima 4 para editar el estado de habitacion \nOprima 5 para salir de este apartado ")
        pedir=(int(input(' ')))
        match pedir:
            case 1:
                tipo_habitacion=input("Ingrese el tipo de la habitacion a cambiar: ")
                precio_habitacion=int(input("Ingrese el precio de la habitacion a cambiar: "))
                estado_habitacion=input("Ingrese el estado de la habitacion a cambiar: ")
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar estos datos: "))
                micursorupdate.execute("update Habitacion set (Tipo_habitacion, Precio_habitacion, Estado_habitacion) = (?,?,?) where Num_habitacion=?",(tipo_habitacion,precio_habitacion,estado_habitacion,ubicacion))
                con.commit()
                con.close()
            case 2:
                tipo_habitacion=input("Ingrese el tipo de habitacion por el cual va a reemplazar el actual: ")
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                micursorupdate.execute("update Habitacion set Tipo_habitacion =? where Num_habitacion =?",(tipo_habitacion,ubicacion))
                con.commit()
                con.close()
            case 3:
                precio_habitacion=int(input("Ingrese el precio de habitacion por el cual va a reemplazar el actual: "))
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                micursorupdate.execute("update Habitacion set Precio_habitacion =? where Num_habitacion =?",(precio_habitacion,ubicacion))
                con.commit()
                con.close()
            case 4:
                estado_habitacion=input("Ingrese el estado de habitacion por el cual va a reemplazar el actual: ")
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                micursorupdate.execute("update Habitacion set Estado_habitacion =? where Num_habitacion =?",(estado_habitacion,ubicacion))
                con.commit()
                con.close()
            case 5:
                break
            case _:
                print("Escoja un numero valido")
        interfaz("pause")

def read():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursorread=con.cursor()
    micursorread.execute("Select * from Habitacion")
    datos=micursorread.fetchall()
    print("Estos son los datos almacenados en la tabla de habitaciones: ")
    for fila in datos:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print("*"*50)
    con.commit()
    con.close()
    
def delete():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursordelete=con.cursor()
    numero=int(input("Ingrese el numero de la habitacion que quiera eliminar: "))
    tipo=input("Ingrese el tipo de la habitacion seleccionada: ")
    precio=int(input("Ingrese el precio de la habitacion seleccionada: "))
    estado=input("Ingrese el estado de la habitacion seleccionada: ")
    micursordelete.execute("delete from Habitacion where Num_habitacion =? and Tipo_habitacion=? and Precio_habitacion=? and Estado_habitacion=?",(numero,tipo,precio,estado))
    con.commit()
    con.close()



