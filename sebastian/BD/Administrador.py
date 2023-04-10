

from sqlite3 import *
from sys import path as ruta
from os import system as interfaz

ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez")
import Clases.Administrador as CA
import Clases.Mesero as CM
import Clases.Recepcionista as CR

#FUNCION PARA AGREGAR UN NUEVO ADMINISTRADOR
def register():
    con1=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursorregister=con1.cursor()
    Numero_Documento=int(input("ingrese el numero de documento del nuevo administrador: "))
    Tipo_Documento=input("ingrese el tipo del documento: ")
    Nombres=input("ingrese los nombres del nuevo administrador: ")
    Apellidos=input("Ingrese los apellidos del nuevo administrador: ")
    Email=input("ingrese el Correo electronico del nuevo administrador: ")
    Contraseña=input("ingrese la contraseña que desea para la cuenta del nuevo administrador: ")
    Funciones=input("Ingrese las funciones que podra tener el nuevo administrador: ")
    Reg=CA.admin(Numero_Documento,Tipo_Documento,Nombres,Apellidos,Email,Contraseña,Funciones)
    register=(Reg.getNum_documento(),Reg.getTipo_documento(),Reg.getNombres(),Reg.getApellidos(),Reg.getEmail(),Reg.getContraseña(),Reg.getFunciones())
    cursorregister.execute("insert into Administrador values(?,?,?,?,?,?,?)", register)
    con1.commit()
    con1.close()
    
    with open("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\\Reportes\\Reporte_administrador.txt","a") as flujo:
        flujo.write("Numero de documento: " + str(Reg.getNum_documento()) +
                    "\nTipo de documento: " + Reg.getTipo_documento() +
                    "\nNombre :" + Reg.getNombres() + 
                    "\nApellido: " + Reg.getApellidos() + 
                    "\nEmail: " + Reg.getEmail() + 
                    "\nContraseña: " + Reg.getContraseña() +
                    "\nFunciones: " + Reg.getFunciones() +
                    "\n" + "*"*50 + 
                    "\n")

#FUNCION PARA AGREGAR UN NUEVO MESERO    
def registermesero():
    con2=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursormesero=con2.cursor()
    Numero_Documento=int(input("ingrese el numero de documento del nuevo mesero: "))
    Tipo_Documento=input("ingrese el tipo del documento: ")
    Nombres=input("ingrese los nombres del nuevo mesero: ")
    Apellidos=input("Ingrese los apellidos del nuevo mesero: ")
    Email=input("ingrese el Correo electronico del nuevo mesero: ")
    Contraseña=input("ingrese la contraseña que desea para la cuenta del nuevo mesero: ")
    Funciones=input("Ingrese las funciones que podra tener el nuevo mesero: ")
    Reg2=CM.Mesero(Numero_Documento,Tipo_Documento,Nombres,Apellidos,Email,Contraseña,Funciones)
    RegMesero=(Reg2.getNum_documento(),Reg2.getTipo_documento(),Reg2.getNombres(),Reg2.getApellidos(),Reg2.getEmail(),Reg2.getContraseña(),Reg2.getFunciones())
    cursormesero.execute("insert into Mesero values (?,?,?,?,?,?,?)", RegMesero)
    con2.commit()
    con2.close()

#FUNCION PARA AGREGAR UN NUEVO RECEPCIONISTA
#NOTA IMPORTANTE: ESTA FUNCION PARA REGISTRAR RECEPCIONISTA SOLO FUNCIONARA SI LA CLASE RECPECIONISTA ESTA CREADA AL MOMENTO DE ESCRIBIR ESTE PROGRAMA LA CLASE NO ESTABA HECHA POR LO TANTO NO
#SE RECOMIENDA SU EJECUCION SIN LA COMPOROBACION DE LA CLASE RECEPCIONISTA
def registerRecepcionista():
    con3=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursorRecepcionista=con3.cursor()
    Numero_Documento=int(input("ingrese el numero de documento del nuevo mesero: "))
    Tipo_Documento=input("ingrese el tipo del documento: ")
    Nombres=input("ingrese los nombres del nuevo mesero: ")
    Apellidos=input("Ingrese los apellidos del nuevo mesero: ")
    Email=input("ingrese el Correo electronico del nuevo mesero: ")
    Contraseña=input("ingrese la contraseña que desea para la cuenta del nuevo mesero: ")
    Funciones=input("Ingrese las funciones que podra tener el nuevo mesero: ")
    Reg3=CR.Recepcionista(Numero_Documento,Tipo_Documento,Nombres,Apellidos,Email,Contraseña,Funciones)
    RegRecepcionista=(Reg3.getNum_doc(),Reg3.getTipo_doc(),Reg3.getNombres(),Reg3.getApellidos(),Reg3.getEmail(),Reg3.getContraseña(),Reg3.getFunciones())
    cursorRecepcionista.execute("insert into Mesero values (?,?,?,?,?,?,?)", RegRecepcionista)
    con3.commit()
    con3.close()


#FUNCION PARA BORRAR ADMINISTRADOR
def deleteAdmin():
    con4=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteAdmin=con4.cursor()
    numero_documento=int(input("Ingrese el numero de documento del administrador que quiera eliminar: "))
    tipo_documento=input("Ingrese el tipo de documento seleccionado: ")
    Nombres=(input("Ingrese el Nombre de el administrador seleccionado: "))
    Apellidos=input("Ingrese el apellido de el adiministrador seleccionado : ")
    cursordeleteAdmin.execute("delete from Administrador where Num_Documento =? and Tipo_Documento=? and Nombres=? and Apellidos=?",(numero_documento,tipo_documento,Nombres,Apellidos))
    con4.commit()
    con4.close()

#A CONTINUACION SOLO HABRA OTRAS VERSIONES DEL PROGRAMA PARA BORRAR ADMINISTRADORES CON LAS DIEFERENCIA DE QUE LOS DATOS REQUERIDOS SERAN MENOS
#ESTO POR SI LA NECESIDAD LO URGE POR FAVOR SOLO USAR EN CASO DE SER NECESARIO.

#SOLO CON EL NOMBRE
'''def deleteAdmin():
    con4=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteAdmin=con4.cursor()
    Nombres=(input("Ingrese el Nombre de el administrador seleccionado: "))
    cursordeleteAdmin.execute("delete from Administrador where Nombres =?",(Nombres)
    con4.commit()
    con4.close()
'''

#SOLO CON NOMBRES Y APELLIDOS
'''def deleteAdmin():
    con4=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteAdmin=con4.cursor()
    Nombres=(input("Ingrese el Nombre de el administrador seleccionado: "))
    Apellidos=input("Ingrese el apellido de el adiministrador seleccionado : ")
    cursordeleteAdmin.execute("delete from Administrador where Nombres =? and Apellidos=?",(Nombres,Apellidos)
    con4.commit()
    con4.close()'''

#CON EL NUMERO DE DOCUMENTO
'''def deleteAdmin():
    con4=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteAdmin=con4.cursor()
    numero_documento=int(input("Ingrese el numero de documento del administrador que quiera eliminar: "))
    cursordeleteAdmin.execute("delete from Administrador where Num_documento =? and Apellidos=?",(numero_documento)
    con4.commit()
    con4.close()'''
#PDT: ESTAS MISMAS FUNCIONES SE PUEDEN ADAPTAR PARA OTROS EMPLEADOS EJ:RECEPCIONISTA,MESERO

#FUNCION PARA BORRAR MESERO
def deleteMesero():
    con5=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteMesero=con5.cursor()
    numero_documento=int(input("Ingrese el numero de documento del Mesero que quiera eliminar: "))
    tipo_documento=input("Ingrese el tipo de documento seleccionado: ")
    Nombres=(input("Ingrese el Nombre de el Mesero seleccionado: "))
    Apellidos=input("Ingrese el apellido de el Mesero seleccionado : ")
    cursordeleteMesero.execute("delete from Mesero where Num_Documento =? and Tipo_Documento=? and Nombres=? and Apellidos=?",(numero_documento,tipo_documento,Nombres,Apellidos))
    con5.commit()
    con5.close()

#FUNCION PARA BORRAR RECEPCIONISTA
def deleteRecepcionista():
    con6=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteRecepcionista=con6.cursor()
    numero_documento=int(input("Ingrese el numero de documento del Recepcionista que quiera eliminar: "))
    tipo_documento=input("Ingrese el tipo de documento seleccionado: ")
    Nombres=(input("Ingrese el Nombre de el Recepcionista seleccionado: "))
    Apellidos=input("Ingrese el apellido de el Recepcionista seleccionado : ")
    cursordeleteRecepcionista.execute("delete from Mesero where Num_Documento =? and Tipo_Documento=? and Nombres=? and Apellidos=?",(numero_documento,tipo_documento,Nombres,Apellidos))
    con6.commit()
    con6.close()


#FUCION PARA CREAR OFERTAS DE HABITACION(HECHA POR NICOLAS MODIFICADA POR JPINZON18)
def createOferta():
    con7=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursorcreateOferta=con7.cursor()
    numero_habitacion=int(input("Ingrese el numero de la habitacion a agregar: "))
    tipo_habitacion=input("Ingrese el tipo de la habitacion a agregar: ")
    precio_habitacion=int(input("Ingrese el precio de la habitacion a agregar: "))
    estado_habitacion=input("Ingrese el estado de la habitacion: ")
    Habit=CA.admin(numero_habitacion,tipo_habitacion,precio_habitacion,estado_habitacion)
    create=(Habit.getNum(),Habit.getTipo(),Habit.getPrecio(),Habit.getEstado())
    cursorcreateOferta.execute("insert into Habitacion values(?,?,?,?)", create)
    con7.commit()
    con7.close()

#FUNCION PARA ELIMINAR OFERTAS DE HABITACION(HECHA POR NICOLAS MODIFICADA POR JPINZON18)
def deleteOferta():
    con8=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteOferta=con8.cursor()
    numero=int(input("Ingrese el numero de la habitacion que quiera eliminar: "))
    tipo=input("Ingrese el tipo de habitacion seleccionada: ")
    precio=int(input("Ingrese el precio de la habitacion seleccionada: "))
    estado=input("Ingrese el estado de la habitacion seleccionada: ")
    cursordeleteOferta.execute("delete from Habitacion where Num_habitacion =? and Tipo_habitacion=? and Precio_habitacion=? and Estado_habitacion=?",(numero,tipo,precio,estado))
    con8.commit()
    con8.close()


#FUNCION PARA CONSULTAR LA TABLA DE HABITACIONES(HECHA POR NICOLAS MODIFICADA POR JPINZON18)
def readOferta():
    con9=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursorreadOferta=con9.cursor()
    cursorreadOferta.execute("Select * from Habitacion")
    datos=cursorreadOferta.fetchall()
    print("Estos son los datos almacenados en la tabla de habitaciones: ")
    for fila in datos:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print("*"*50)
    con9.commit()
    con9.close()

#FUNCION PARA ACTUALIZAR LAS HABITACIONES(HECHA POR NICOLAS MODIFICADA POR JPINZON18)
def updateOferta():
    while True:
        interfaz("cls")
        con10=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
        cursorupdateOferta=con10.cursor()
        print("¿Cual es la columna que desea actualizar? \nOprima 1 para editar el tipo de habitacion \nOprima 2 para editar el precio de habitacion \nOprima 3 para editar el estado de habitacion \nOprima 4 para salir de este apartado ")
        pedir=(int(input(' ')))
        match pedir:
            case 1:
                tipo_habitacion=input("Ingrese el tipo de habitacion por el cual va a reemplazar el actual: ")
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                cursorupdateOferta.execute("update Habitacion set Tipo_habitacion =? where Num_habitacion =?",(tipo_habitacion,ubicacion))
                con10.commit()
                con10.close()
            case 2:
                precio_habitacion=int(input("Ingrese el precio de habitacion por el cual va a reemplazar el actual: "))
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                cursorupdateOferta.execute("update Habitacion set Precio_habitacion =? where Num_habitacion =?",(precio_habitacion,ubicacion))
                con10.commit()
                con10.close()
            case 3:
                estado_habitacion=input("Ingrese el estado de habitacion por el cual va a reemplazar el actual: ")
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                cursorupdateOferta.execute("update Habitacion set Estado_habitacion =? where Num_habitacion =?",(estado_habitacion,ubicacion))
                con10.commit()
                con10.close()
            case 4:
                break
            case _:
                print("Escoja un numero valido")
        interfaz("pause")

#FUNCION PARA ElIMINAR LAS HABITACIONES(HECHA POR NICOLAS MODIFICADA POR JPINZON18)
def deleteOferta():
    con11=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    cursordeleteOferta=con11.cursor()
    numero=int(input("Ingrese el numero de la habitacion que quiera eliminar: "))
    tipo=input("Ingrese el tipo de habitacion seleccionada: ")
    precio=int(input("Ingrese el precio de la habitacion seleccionada: "))
    estado=input("Ingrese el estado de la habitacion seleccionada: ")
    cursordeleteOferta.execute("delete from Habitacion where Num_habitacion =? and Tipo_habitacion=? and Precio_habitacion=? and Estado_habitacion=?",(numero,tipo,precio,estado))
    con11.commit()
    con11.close()
