import sqlite3
with sqlite3.connect('E:\Vasquez\BDsibo')as con:
    micursor=con()
    sentencia="SELECT * FROM cliente"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_cliente):
    micursor=connetc.cursor()
    sentencia=f"update {tabla} SET {campo}='{dato}' WHERE id_cliente ='{id_cliente}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa')
'''modificar(con,'cliente','',)'''

def eliminar (connetc,tabla,campo,dato,id_cliente):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa')
'''eliminar'''
def insertar(id_cliente,id_habitacion,nombre,apellido,correo_electronico,telefono,direccion):
    micursor=connetc.cursor()
    sentencia=f"INSERT INTO cliente VALUES ({id_cliente},'{id_habitacion}','{nombre}','{apellido}','{correo_electronico}','{telefono}','{direccion}','{id_cliente})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')

    '''insertar()'''

    def leer():
        micursor=con.cursor()
        sentencia=f"SELECT * FROM cliente"
        micursor.execute(sentencia)
        datos=micursor.fetchall()
        con.commit()
        print(datos)

    leer()