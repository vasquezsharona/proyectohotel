
from sqlite3 import *
from sys import path as ruta
from os import system as interfaz

ruta.append("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL")
import Clases.Servicios as CS



def create():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursorcreate=con.cursor()
    numero_documento=int(input("Ingrese el numero de documento del cliente: "))
    lavanderia=int(input("Ingrese el precio si el cliente hizo uso de servicio de lavanderia: "))
    piscina=int(input("Ingrese el precio si el cliente hizo uso de la piscina: "))
    zona_recreativa=int(input("Ingrese el precio si el cliente hizo uso de la zona recreativa: "))
    aparatos_domesticos=int(input("Ingrese el precio si el cliente hizo uso de aparatos domesticos: "))
    minibar=int(input("Ingrese precio si el cliente hizo uso del minibar: "))
    restaurante=int(input("Ingrese precio si el cliente hizo uso del restaurante: "))
    servicio_habitacion=int(input("Ingrese precio si el cliente hizo uso de servicio de habitacion adicional: "))
    alquiler_carros=int(input("Ingrese precio si el cliente hizo uso del alquiler de carros: "))
    ubicacion=numero_documento
    create=(numero_documento,lavanderia,piscina,zona_recreativa,aparatos_domesticos,minibar,restaurante,servicio_habitacion,alquiler_carros)
    micursorcreate.execute("insert into Servicios (Num_Doc,Lavanderia,Piscina,Zona_recreativa,Aparatos_domesticos,Minibar,Restaurante,Servicio_habitacion,Alquiler_carros) values (?,?,?,?,?,?,?,?,?)",(numero_documento,lavanderia,piscina,zona_recreativa,aparatos_domesticos,minibar,restaurante,servicio_habitacion,alquiler_carros))
    
    micursorcreate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
    
    datos=micursorcreate.fetchall()[0]

    costo_total= 0
    for i in range(1,10):
        costo_total+=datos[i]
    print(costo_total)

    micursorcreate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,ubicacion))
    
    con.commit()
    
    Servicios=CS.Servicios(numero_documento,lavanderia,piscina,zona_recreativa,aparatos_domesticos,minibar,restaurante,servicio_habitacion,alquiler_carros,costo_total)
    con.close()
    
    with open("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\rodriguez\PROYECTO_FINAL\\Reportes\\Reporte_servicios.txt","a") as flujo:
        flujo.write("Numero de documento: " + str(Servicios.getNumdoc()) + 
                    "\nLavanderia: " + str(Servicios.getLavanderia()) + 
                    "\nPiscina: " + str(Servicios.getPiscina()) + 
                    "\nZona Recreativa: " + str(Servicios.getZonarecre()) + 
                    "\nAparatos domesticos: " + str(Servicios.getApardome()) + 
                    "\nMinibar: " + str(Servicios.getMinibar()) + 
                    "\nRestaurante: " + str(Servicios.getRestaurante()) + 
                    "\nServicio de habitacion: " + str(Servicios.getServicioHabi()) + 
                    "\nAlquiler de carros: " + str(Servicios.getAlquilercarro()) + 
                    "\nCosto total: " + str(Servicios.getPrecio()) + 
                    "\n" + "*"*50 +
                    "\n")


def update():
    while True:
        con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
        micursorupdate=con.cursor()
        print("¿Cual es la columna que desea actualizar? \nOprima 1 para editar una columna entera \nOprima 2 para editar el numero de documento \nOprima 3 para editar el servicio de lavanderia \nOprima 4 para editar los gastos en piscina \nOprima 5 para editar los gastos en zona recreatica \nOprima 6 para editar los gastos en aparatos domesticos \nOprima 7 para editar los gastos en minibar \nOprima 8 para editar los gastos en restaurante \nOprima 9 para editar los gastos en servicio de habitacion \nOprima 10 para editar los gastos en alquiler de carros \nOprima 11 para salir del programa")
        pedir=int(input(" "))
        match pedir:
            case 1:
                ubicacion=int(input("Ingrese el numero de documento antiguo: "))
                numero_documento=int(input("Ingrese el numero de documento nuevo del cliente: "))
                lavanderia=int(input("Ingrese el precio a actualizar de servicio de lavanderia: "))
                piscina=int(input("Ingrese el precio a actualizar de la piscina: "))
                zona_recreativa=int(input("Ingrese el precio a actualizar de la zona recreativa: "))
                aparatos_domesticos=int(input("Ingrese el precio a actualizar de aparatos domesticos: "))
                minibar=int(input("Ingrese precio a actualizar del minibar: "))
                restaurante=int(input("Ingrese precio a actualizar del restaurante: "))
                servicio_habitacion=int(input("Ingrese precio a actualizar de servicio de habitacion adicional: "))
                alquiler_carros=int(input("Ingrese precio a actualizar del alquiler de carros: "))
                ubicacion=numero_documento
                update=(numero_documento,lavanderia,piscina,zona_recreativa,aparatos_domesticos,minibar,restaurante,servicio_habitacion,alquiler_carros,ubicacion)
                micursorupdate.execute("update Servicios set (Num_Doc,Lavanderia,Piscina,Zona_recreativa,Aparatos_domesticos,Minibar,Restaurante,Servicio_habitacion,Alquiler_carros) = (?,?,?,?,?,?,?,?,?) where Num_Doc =?",update)
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(numero_documento, ))
    
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 2:
                ubicacion=int(input("Ingrese el numero de documento antiguo: "))
                numero_documento=int(input("Ingrese el numero de documento nuevo del cliente: "))
                micursorupdate.execute("update Servicios set (Num_Doc) = (?)",(numero_documento,ubicacion))
                con.commit()
                con.close()
            case 3:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                lavanderia=int(input("Ingrese el precio a actualizar de servicio de lavanderia: "))
                micursorupdate.execute("update Servicios set (Lavanderia) = (?) where Num_Doc =?",(lavanderia,ubicacion))
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
    
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 4:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                piscina=int(input("Ingrese el precio a actualizar de servicio de piscina: "))
                micursorupdate.execute("update Servicios set (Piscina) = (?)",(piscina,ubicacion))
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 5:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                zona_recreativa=int(input("Ingrese el precio a actualizar de la zona recreativa: "))
                micursorupdate.execute("update Servicios set (Zona_recreativa) = (?) where Num_Doc =?",(zona_recreativa,ubicacion))
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 6:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                aparatos_domesticos=int(input("Ingrese el precio a actualizar de aparatos domesticos: "))
                micursorupdate.execute("update Servicios set (Aparatos_domesticos) = (?) where Num_Doc =?",(aparatos_domesticos,ubicacion))
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 7:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                minibar=int(input("Ingrese precio a actualizar del minibar: "))
                micursorupdate.execute("update Servicios set (Minibar) = (?) where Num_Doc =?",minibar,ubicacion)
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 8:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                restaurante=int(input("Ingrese precio a actualizar del restaurante: "))
                micursorupdate.execute("update Servicios set (Restaurante) = (?) where Num_Doc =?",(restaurante,ubicacion))
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 9:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                servicio_habitacion=int(input("Ingrese precio a actualizar de servicio de habitacion adicional: "))
                micursorupdate.execute("update Servicios set (Servicio_habitacion) = (?) where Num_Doc =?",(servicio_habitacion,ubicacion))
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 10:
                ubicacion=int(input("Ingrese el numero de documento del cliente: "))
                alquiler_carros=int(input("Ingrese precio a actualizar del alquiler de carros: "))
                micursorupdate.execute("update Servicios set (Alquiler_carros) = (? where Num_Doc =?",(alquiler_carros,ubicacion))
                micursorupdate.execute("select * from Servicios where Num_Doc=?",(ubicacion, ))
                datos=micursorupdate.fetchall()[0]

                costo_total= 0
                for i in range(1,10):
                    costo_total+=datos[i]
                print(costo_total)

                micursorupdate.execute("update Servicios set Costo_servicios =? where Num_Doc =?",(costo_total,numero_documento))
                con.commit()
                con.close()
            case 11:
                break
            case _:
                print("Ingrese un numero valido")
        interfaz("pause")
        

def read():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursorread=con.cursor()
    micursorread.execute("Select * from Servicios")
    datos=micursorread.fetchall()
    print("Estos son los datos almacenados en la tabla de servicio: ")
    for fila in datos:
        print("Num_Doc: ",fila[0])
        print("Lavanderia: ",fila[1])
        print("Piscina: ",fila[2])
        print("Zona recreativa: ",fila[3])
        print("Aparatos domesticos: ",fila[4])
        print("Minibar: ",fila[5])
        print("Restaurante: ",fila[6])
        print("Servicio habitacion: ",fila[7])
        print("Alquiler carros: ",fila[8])
        print("Costo total: ",fila[9])
        print("*"*50)
    con.commit()
    con.close()

def delete():
    con=connect("C:\Users\osa marcela\Desktop\python_sharon\1\proyecto_siboshasebcar\vasquez\BDsibo")
    micursordelete=con.cursor()
    numero_documento=int(input("Ingrese el numero de documento del cliente a eliminar: "))
    lavanderia=int(input("Seleccione el precio del uso de la lavanderia del cliente seleccionado: "))
    piscina=int(input("Seleccione el precio del uso de la piscina del cliente seleccionado: "))
    zona_recreativa=int(input("Seleccione el precio del uso de la zona recreativa del cliente seleccionado: "))
    aparatos_domesticos=int(input("Seleccione el precio del uso de los aparatos domesticos del cliente seleccionado: "))
    minibar=int(input("Seleccione el precio del uso de minibar del cliente seleccionado: "))
    restaurante=int(input("Seleccione el precio del uso de restaurante del cliente seleccionado: "))
    servicio_habitacion=int(input("Seleccione el precio del uso de servicio de habitacion adicional del cliente seleccionado: "))
    alquiler_carros=int(input("Seleccion el precio del uso de alquiler de carros del cliente selecionado: "))
    costo_servicios=int(input("Seleccione el costo toal de los servicios del cliente seleccionado: "))
    ubicacion=numero_documento
    micursordelete.execute("delete from Servicios where Num_Doc =? and Lavanderia=? and Piscina=? and Zona_Recreativa=? and Aparatos_domesticos=? and Minibar=? and Restaurante=? and Servicio_habitacion=? and Alquiler_carros=? and Costo_servicios=?",(numero_documento,lavanderia,piscina,zona_recreativa,aparatos_domesticos,minibar,restaurante,servicio_habitacion,alquiler_carros,costo_servicios))
    con.commit()
    con.close()




