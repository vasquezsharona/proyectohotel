
from sqlite3 import *
from sys import path as ruta
from os import system as interfaz

ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL")
import Clases.Mesero as CM

def create():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursorcreate=con.cursor()
    numero_documento=int(input("Ingrese el numero de documento a agregar: "))
    tipo_documento=input("Ingrese el tipo de documento a agregar: ")
    nombre=input("Ingrese el nombre del mesero :")
    apellido=input("Ingrese el apellido del mesero: ")
    email=input("Ingrese el correo electronico del mesero: ")
    contraseña=input("Ingrese la contraseña de su cuenta: ")
    funciones=input("Ingrese las funciones del mesero: ")
    Mesero=CM.Mesero(numero_documento,tipo_documento,nombre,apellido,email,contraseña,funciones)
    create=(Mesero.getNum_documento(),Mesero.getTipo_documento(),Mesero.getNombres(),Mesero.getApellidos(),Mesero.getEmail(),Mesero.getContraseña(),Mesero.getFunciones())
    micursorcreate.execute("insert into Mesero values (?,?,?,?,?,?,?)",(create))
    con.commit()
    con.close()
    
    with open("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL\\Reportes\\Reporte_mesero.txt","a") as flujo:
        flujo.write("Numero de documento: " + str(Mesero.getNum_documento()) +
                    "\nTipo de documento: " + Mesero.getTipo_documento() +
                    "\nNombre: " + Mesero.getNombres() + 
                    "\nApellido: " + Mesero.getApellidos() + 
                    "\nEmail: " + Mesero.getEmail() + 
                    "\nContraseña: " + Mesero.getContraseña() + 
                    "\nFunciones:" + Mesero.getFunciones() + 
                    "\n" + "*"*50 + 
                    "\n")


def update():
    while True:
        interfaz("cls")
        con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
        micursorupdate=con.cursor()
        print("¿Cual es la columna que desea actualizar? \nOprima 1 para editar una columna entera \nOprima 2 para editar el numero de documento \nOprima 3 para editar el tipo de documento \nOprima 4 para editar los nombres \nOprima 5 para editar los apellidos \nOprima 6 para editar el email \nOprima 7 para editar la contraseña \nOprima 8 para editar las funciones \nOprima 9 para salir de este menu")
        pedir=int(input(" "))
        match pedir:
            case 1:
                ubicacion=int(input("Ingrese el numero de documento antiguo: "))
                numero_documento=int(input("Ingrese el numero de documento nuevo: "))
                tipo_documento=int(input("Ingrese el tipo de documento nuevo: "))
                nombre=input("Ingrese el nombre del mesero nuevo:")
                apellido=input("Ingrese el apellido del mesero nuevo: ")
                email=input("Ingrese el correo electronico del mesero nuevo: ")
                contraseña=input("Ingrese la contraseña nueva: ")
                funciones=input("Ingrese las funciones del mesero nuevas: ")
                micursorupdate.execute("update Mesero set (Num_documento, Tipo_documento, Nombres, Apellidos, Email, Contraseña, Funciones) = (?,?,?,?,?,?,?) where Num_documento =?",(numero_documento,tipo_documento,nombre,apellido,email,contraseña,funciones,ubicacion))
                con.commit()
                con.close()
            case 2:
                ubicacion=int(input("Ingrese el numero de documento antiguo: "))
                numero_documento=int(input("Ingrese el numero de documento nuevo: "))
                micursorupdate.execute("update Mesero set Num_documento = ? where Num_documento =?",(numero_documento,ubicacion))
                con.commit()
                con.close()
            case 3:
                tipo_documento=input("Ingrese el tipo de documento nuevo: ")
                ubicacion=int(input("Ingrese el numero de documento del mesero al que le va a realizar el cambio: "))
                micursorupdate.execute("update Mesero set Tipo_documento = ? where Num_documento =?",(tipo_documento,ubicacion))
            case 4:
                nombre=input("Ingrese el nombre del mesero nuevo:")
                ubicacion=int(input("Ingrese el numero de documento del mesero al que le va a realizar el cambio: "))
                micursorupdate.execute("update Mesero set Nombres = ? where Num_documento =?",(nombre,ubicacion))
            case 5:
                apellido=input("Ingrese el apellido del mesero nuevo: ")
                ubicacion=int(input("Ingrese el numero de documento del mesero al que le va a realizar el cambio: "))
                micursorupdate.execute("update Mesero set Apellidos = ? where Num_documento =?",(apellido,ubicacion))
            case 6:
                email=input("Ingrese el correo electronico del mesero nuevo: ")
                ubicacion=int(input("Ingrese el numero de documento del mesero al que le va a realizar el cambio: "))
                micursorupdate.execute("update Mesero set Email = ? where Num_documento =?",(email,ubicacion))
            case 7:
                contraseña=input("Ingrese la contraseña nueva: ")
                ubicacion=int(input("Ingrese el numero de documento del mesero al que le va a realizar el cambio: "))
                micursorupdate.execute("update Mesero set Contraseña = ? where Num_documento =?",(contraseña,ubicacion))
            case 8:
                funciones=input("Ingrese las funciones del mesero nuevas: ")
                ubicacion=int(input("Ingrese el numero de documento del mesero al que le va a realizar el cambio: "))
                micursorupdate.execute("update Mesero set Funciones = ? where Num_documento =?",(funciones,ubicacion))
            case 9:
                break
            case _:
                print("Escoja un numero valido")
        interfaz("pause")

def read():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursorread=con.cursor()
    micursorread.execute("Select * from Mesero")
    datos=micursorread.fetchall()
    print("Estos son los datos almacenados en la tabla de mesero: ")
    for fila in datos:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print(fila[4])
        print(fila[5])
        print(fila[6])
        print("*"*50)
    con.commit()
    con.close()


def delete():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursordelete=con.cursor()
    numero_documento=int(input("Ingrese el numero de documento que quiere eliminar: "))
    tipo_documento=int(input("Ingrese el tipo de documento del numero de documento seleccionado: "))
    nombre=input("Ingrese el nombre del mesero del numero de documento seleccionado:")
    apellido=input("Ingrese el apellido del mesero del numero de documento seleccionado: ")
    email=input("Ingrese el correo electronico del mesero del numero de documento seleccionado: ")
    contraseña=input("Ingrese la contraseña de la cuenta del numero de documento seleccionado: ")
    funciones=input("Ingrese las funciones del mesero del numero de documento seleccionado: ")
    micursordelete.execute("delete from Mesero where Num_documento =? and Tipo_Documento=? and Nombres=? and Apellidos=? and Email=? and Contraseña=? and Funciones=?",(numero_documento,tipo_documento,nombre,apellido,email,contraseña,funciones))
    con.commit()
    con.close()