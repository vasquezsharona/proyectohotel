import sqlite3
with sqlite3.connect('E:\Vasquez\BDsibo')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM reservas"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_reservas):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_reservas ='{id_reservas}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa')
'''modificar(con,'reservas','',)'''

def eliminar (connetc,tabla,campo,dato,id_reservas):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa')
'''eliminar(con,'reservas')'''

def insertar(id_reservas,id_cliente,id_habitacion,fecha_entraada,fecha_salida,cantidad_personas,total_reservas):
	micursor=connetc.cursor()
    sentencia=f"INSERT INTO reservas VALUES ({id_reservas},'{id_cliente}','{id_habitacion}','{fecha_entraada}','{fecha_salida}','{cantidad_personas}','{total_reservas})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')
    '''insertar()'''

    def leer():
        micursor=con.cursor()
        sentencia=f"SELECT * FROM reservas"
        micursor.execute(sentencia)
        datos=micursor.fetchall()
        con.commit()
        print(datos)

    leer()