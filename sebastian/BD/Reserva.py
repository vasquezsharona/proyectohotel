
from sqlite3 import *
from sys import path as ruta
from os import system as interfaz

ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL")
import Clases.Reserva as CR



def create():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    
    micursorcreate=con.cursor()
    numero_documento=int(input("Ingrese el numero de documento del cliente: "))
    numero_habitacion=int(input("Ingrese el numero de habitacion reservada: "))
    fecha_entrada=input("Ingrese la fecha de comienzo de la reserva: ")
    fecha_salida=input("Ingrese la fecha de finalizacion de la reserva: ")
    costo_servicios=int(input("Ingrese el costo total de los servicios: "))
    precio_reserva=int(input("Ingrese el precio total de la reserva: "))
    metodo_pago=input("Ingrese el metodo de pago seleccionado: ")
    
    micursorcreate.execute("insert into Reserva (Num_Doc, Num_habitacion, Fecha_Entrada, Fecha_Salida, Costo_servicios, Precio_Reserva, Metodos_Pago) values (?,?,?,?,?,?,?)",(numero_documento,numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,precio_reserva,metodo_pago))
    con.commit()
    
    micursorcreate.execute("select ID_Reserva from Reserva where Num_Doc =? and Num_habitacion =? and Fecha_Entrada =? and Fecha_Salida =? and Costo_servicios =? and Metodos_Pago =?",(numero_documento,numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,metodo_pago))
    dato=micursorcreate.fetchone()
    for i in dato:
        id_reserva=i
    
    #PROCESO PARA AUTOMATIZAR EL PRECIO TOTAL DE LA RESERVA (NO FUNCIONA)
    
    """ubicacion=id_reserva
    micursorcreate.execute("select Precio_habitacion, Costo_servicios from Habitacion as HB INNER JOIN Reserva as RE ON HB.Num_habitacion=RE.Num_habitacion where ID_Reserva =?",ubicacion)
    datos2=micursorcreate.fetchall()[0]
    

    precio_reserva=0
    for valor in datos2:
        precio_reserva+=valor
        
    micursorcreate.execute("update Reserva set Precio_Reserva =? where ID_Reserva =?",(precio_reserva,ubicacion))"""

    con.commit()
    Reserva=CR.Reserva(id_reserva,numero_documento,numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,precio_reserva,metodo_pago)
    
    print("Reserva creada con exito :D")
    con.close()
    
    with open("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL\\Reportes\\Reporte_reserva.txt","a") as flujo:
        flujo.write("ID de la reserva: " + str(Reserva.getId()) + 
                    "\nNumero de documento del cliente: " + str(Reserva.getNum_doc()) + 
                    "\nNumero de habitacion reservada: " + str(Reserva.getNum_hab()) +
                    "\nFecha de inicio de la reserva: " + Reserva.getFecha_e() + 
                    "\nFecha de finalizacion de la reserva: " + Reserva.getFecha_s() + 
                    "\nCosto total de los servicios: " + str(Reserva.getCosto_s()) + 
                    "\nPrecio total de la reserva: " + str(Reserva.getPrecio()) + 
                    "\nMetodo de pago para la reserva: " + Reserva.getMetodo() +
                    "\n" + "*"*50 +
                    "\n")



def update():
    while True:
        interfaz("cls")
        con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
        micursorupdate=con.cursor()
        print("¿Cual es la columna que desea actualizar? \nOprima 1 para editar una columna completa \nOprima 2 para editar el numero de habitacion \nOprima 3 para editar la fecha de entrada \nOprima 4 para editar la fecha de salida \nOprima 5 para editar los costos de los servicios \nOprima 6 para editar el metodo de pago \nOprima 7 para salir de este apartado")
        pedir=(int(input(' ')))
        match pedir:
            case 1:
                numero_habitacion=int(input("Ingrese el numero de habitacion a actualizar: "))
                fecha_entrada=input("Ingrese la fecha de comienzo de la reserva a actualizar: ")
                fecha_salida=input("Ingrese la fecha de finalizacion de la reserva a actualizar: ")
                costo_servicios=int(input("Ingrese el costo total de los servicios a actualizar: "))
                precio_reserva=int(input("Ingrese el nuevo precio total de la reserva: "))
                metodo_pago=input("Ingrese el metodo de pago seleccionado a actualizar: ")
                ubicacion=int(input("Ahora ingrese el ID de la reserva en la que se van a hacer estos cambios :"))
                micursorupdate.execute("update Reserva set (Num_habitacion, Fecha_Entrada, Fecha_Salida, Costo_servicios, Precio_Reserva, Metodos_Pago) = (?,?,?,?,?,?) where ID_Reserva = ?",(numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,precio_reserva,metodo_pago,ubicacion))
                con.commit()
                con.close()
            case 2:
                numero_habitacion=int(input("Ingrese el numero de habitacion a actualizar: "))
                precio_reserva=int(input("Ahora ingrese el nuevo precio de reserva: "))
                ubicacion=int(input("Ahora ingrese el ID de la reserva en la que se van a hacer estos cambios :"))
                micursorupdate.execute("update Reserva set (Num_habitacion, Precio_Reserva) =(?,?) where ID_Reserva = ?",(numero_habitacion,precio_reserva,ubicacion))
                con.commit()
                con.close()
            case 3:
                fecha_entrada=input("Ingrese la fecha de comienzo de la reserva a actualizar: ")
                ubicacion=int(input("Ahora ingrese el ID de la reserva en la que se van a hacer estos cambios :"))
                micursorupdate.execute("update Reserva set Fecha_Entrada =? where ID_Reserva = ?",(fecha_entrada,ubicacion))
                con.commit()
                con.close()
            case 4:
                fecha_salida=input("Ingrese la fecha de finalizacion de la reserva a actualizar: ")
                ubicacion=int(input("Ahora ingrese el ID de la reserva en la que se van a hacer estos cambios :"))
                micursorupdate.execute("update Reserva set Fecha_Salida =? where ID_Reserva = ?",(fecha_salida,ubicacion))
                con.commit()
                con.close()
            case 5:
                costo_servicios=int(input("Ingrese el costo total de los servicios a actualizar: "))
                precio_reserva=int(input("Ahora ingrese el nuevo precio de reserva: "))
                ubicacion=int(input("Ahora ingrese el ID de la reserva en la que se van a hacer estos cambios :"))
                micursorupdate.execute("update Reserva set (Costo_servicios, Precio_Reserva) = (?,?) where ID_Reserva = ?",(costo_servicios,precio_reserva,ubicacion))
                con.commit()
                con.close()
            case 6:
                metodo_pago=input("Ingrese el metodo de pago seleccionado a actualizar: ")
                ubicacion=int(input("Ahora ingrese el ID de la reserva en la que se van a hacer estos cambios :"))
                micursorupdate.execute("update Reserva set Metodos_Pago =? where ID_Reserva = ?",(metodo_pago,ubicacion))
                con.commit()
                con.close()
            case 7:
                break
            case _:    
                print("Escoja un numero valido")
        interfaz("pause")
        

def read():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursorread=con.cursor()
    micursorread.execute("Select * from Reserva")
    datos=micursorread.fetchall()
    print("Estos son los datos almacenados en la tabla de reserva: ")
    for fila in datos:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print(fila[4])
        print(fila[5])
        print(fila[6])
        print(fila[7])
        print("*"*50)
    con.commit()
    con.close()
    
def delete():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursordelete=con.cursor()
    id_reserva=int(input("Ingrese el id de la reserva que desea eliminar: "))
    numero_documento=int(input("Ingrese el numero de documento del cliente de la reserva seleccionada: "))
    numero_habitacion=int(input("Ingrese el numero de habitacion de la reserva seleccionada: "))
    fecha_entrada=input("Ingrese la fecha de comienzo de la reserva seleccionada: ")
    fecha_salida=input("Ingrese la fecha de finalizacion de la reserva seleccionada: ")
    costo_servicios=int(input("Ingrese el costo total de los servicios de la reserva seleccionada: "))
    precio_reserva=int(input("Ingrese el precio total de la reserva seleccionada: "))
    metodo_pago=input("Ingrese el metodo de pago de la reserva seleccionada: ")
    micursordelete.execute("delete from Reserva where ID_Reserva =? and Num_Doc=? and Num_habitacion=? and Fecha_Entrada=? and Fecha_Salida=? and Costo_servicios=? and Precio_Reserva=? and Metodos_Pago=?",(id_reserva,numero_documento,numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,precio_reserva,metodo_pago))
    con.commit()
    con.close()