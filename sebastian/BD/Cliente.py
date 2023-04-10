from sqlite3 import *
from sys import path as ruta
from os import system as interfaz

ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez")
import Clases.Cliente as CL

def agregarcliente():                                                                                                       
    conA=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    curs=conA.cursor()
    Num_Doc=int(input("Ingrese el numero de documento: "))
    Tipo_Doc=input("Ingrese el tipo de documento: ")
    Nombres=input("Ingrese nombre: ")
    Apellidos=input("Ingrese apellido: ")
    Correo=input("Ingrese correo: ")
    Contraseña=input("Ingrese contraseña: ")
    cli=CL.cliente(Num_Doc,Tipo_Doc,Nombres,Apellidos,Correo,Contraseña)
    create1=(cli.getNum_doc(),cli.getTipo_doc(),cli.getNombres(),cli.getApellidos(),cli.getCorreo(),cli.getContraseña())
    curs.execute('insert into Cliente values(?,?,?,?,?,?)',create1)
    conA.commit()
    conA.close()
    
    with open(":\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\\Reportes\\Reporte_cliente.txt","a") as flujo:
        flujo.write("Numero de documento: " + str(cli.getNum_doc()) + 
                    "\nTipo de documento: " + cli.getTipo_doc() + 
                    "\nNombre: " + cli.getNombres() + 
                    "\nApellido: " + cli.getApellidos() + 
                    "\nCorreo: " + cli.getCorreo() + 
                    "\nContraseña: " + cli.getContraseña() + 
                    "\n" + "*"*50 + 
                    "\n")


def verdatos():                                                                                                             
    conB=connect('C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo')
    cursread=conB.cursor()
    cursread.execute("Select * from Cliente")
    datos=cursread.fetchall()
    print("Estos son los datos en la tabla de clientes: ")
    for fila in datos:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print(fila[4])
        print(fila[5])
        print("*"*50)
    conB.commit()
    conB.close()

#elejir una columna para buscar dentro de ella un dato especifico de un cliente
def seleccion():
    conF=connect('C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo')
    cursleer=conF.cursor()
    campo=input('en que columna quiere buscar? ')
    dato=input('ingrese el dato del cliente: ')
    sentencia=f"SELECT * FROM Cliente WHERE {campo}='{dato}'"
    lista=cursleer.execute(sentencia)
    return lista.fetchall()


def delete():
    conD=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursdel=conD.cursor()
    numero=int(input("Ingrese el numero de documetno de el usuario a eliminar: "))
    cursdel.execute("delete from Cliente where Num_Doc =? ",(numero))
    conD.commit()
    conD.close()



def actualizar():                                                                                                                                           #actualizar
    while True:
        interfaz("cls")
        conD=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
        cursactu=conD.cursor()
        print("¿Cual es la columna que desea actualizar? \nOprima 1 para editar el Numero de documento \nOprima 2 para editar el tipo de documento \nOprima 3 para editar el nombre \nOprima 4 para editar apellido \nOprima 5 para editar correo \nOprima 6 para editar contraseña \noprima 7 para salir de este apartado")
        pedir=(int(input(' ')))
        match pedir:
            case 1:
                a=int(input("Ingrese el numero de documento actual: "))
                b=int(input("Ingrese el numero de documento nuevo: "))
                cursactu.execute("update Cliente set Num=? where Num_Doc=?",(b,a))
                conD.commit()
                conD.close()
            case 2:
                c=int(input("Por favor ingrese el número de documento que desea cambiar el tipo de documento: "))
                d=(input("Por favor ingrese el nuevo tipo de documento: "))
                cursactu.execute("update Cliente set Tipo_Doc =? where Num_Doc =?",(d,c))
                conD.commit()
                conD.close()
            case 3:
                e=int(input("Por favor ingrese el número de documento que desea cambiar el nombre: "))
                f=(input("Por favor ingrese el nuevo nombre: "))
                cursactu.execute("update Cliente set Nombres =? where Num_Doc =?",(f,e))
                conD.commit()
                conD.close()
            case 4:
                g=int(input("Por favor ingrese el número de documento que desea cambiar el apellido: "))
                h=(input("Por favor ingrese el nuevo apellido: "))
                cursactu.execute("update Cliente set Apellidos =? where Num_Doc =?",(h,g))
                conD.commit()
                conD.close()
            case 5:
                i=int(input("Por favor ingrese el número de documento que desea cambiar el correo: "))
                j=(input("Por favor ingrese el nuevo correo: "))
                cursactu.execute("update Cliente set Correo =? where Num_Doc =?",(j,i))
                conD.commit()
                conD.close()
            case 6:
                k=int(input("Por favor ingrese el número de documento que desea cambiar la comtraseña: "))
                l=(input("Por favor ingrese la nueva contraseña: "))
                cursactu.execute("update Cliente set Contraseña =? where Num_Doc =?",(l,k))
                conD.commit()
                conD.close()
            case 7:
                break
            case _:
                print("Escoja un numero valido")
        interfaz("pause")