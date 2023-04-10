import sqlite3
from os import system
import time

database = "Hotel.db"
 
class DB:
    def ejecutar_consulta(self,consulta,parametros=()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            result=self.cursor.execute(consulta,parametros)
            conn.commit()
            return result 

db=DB()
result = db.ejecutar_consulta("SELECT * FROM Recepcionista")
print(result.fetchall())

db=DB()
result = db.ejecutar_consulta("SELECT * FROM Recepcionista")
print(result.fetchall())

def create():
    Num_Documento = str(input("ingrese su numero de documento:"))
    Tipo_Documento =str(input("ingrese su tipo de documento:"))
    Nombres =str(input("ingrese su nombre: "))
    Apellidos = str(input("ingrese su apellido:"))
    Email = str(input("ingrese su email:"))
    Contraseña = str(input("ingrese su contraseña:"))
    Funciones = str(input("ingrese su funcion:"))
    if(len(Num_Documento)> 0 and len(Tipo_Documento) > 0 , len(Nombres) > 0 and len(Apellidos)>0 ,len(Email)>0 or len(Contraseña) and len(Funciones)>0):
        sql=("INSERT INTO recepcionista(Num_Documento,Tipo_Documento,Nombres,Apellido,Email,Contraseña,Funciones)VAlUES(?,?)")
        parametros=(Num_Documento,Tipo_Documento,Nombres,Apellidos,Email,Contraseña,Funciones)
        db.ejecutar_consulta(sql,parametros)
        print("insertados...")
def read():
    result=db.ejecutar_consulta("SELCT * FROM Recepcionista")
    for data in result:
        print("""
        Num_Documento:{}
        Tipo_Documento:{}
        Nombre:{}
        Apellido:{}
        Email:{}
        Contraseña:{}
        Funciones:{} """.format(data[0],data[1],data[2]))

def update():
    Num_Documento=int(input("Ingrese el numero de documento"))
    Tipo_Documento=int(input("Ingrese el tipo de documento"))
    Nombre=int(input("Ingrese su nombre"))
    Apellido=int(input("Ingrese su apellido"))
    Email=int(input("Ingrese el email"))
    Contraseña=int(input("Ingrese su contraseña"))
    Funciones=int(input("Ingrese su funcion"))
    if(Num_Documento != 0):
        sql="UPDATE Recepcionista SET Tipo_Documento=?,Nombres=?,Apellido=?,Email=?,Contraseña=?,Funciones=? WHERE Num_Documento=?"
        parametros=(Num_Documento,Tipo_Documento,Nombre,Apellido,Email,Contraseña,Funciones)
        db.ejecutar_consulta(sql,parametros)
        print("Actualizados!")
    
def delete():
    id= int(input("ingrese el Num_Documento:"))
    if (id != 0):
        sql="DELETE FROM Recepcionista WHERE Num_Documento=?"
        parametros=(id,)
        db.ejecutar_consulta(sql,parametros)
        print("Eleminados!")
    
def search():
    Nombres=str(input("ingrese su nombre:"))
    if (len(Nombres)>0):
        sql="SELECT * FROM  Recepcionista WHERE Nombres LIKE ?:"
        parametros=("%%".format(Nombres),)
        result=db.ejecutar_consulta(sql,parametros)
        print("""
        +Num_Documento:{}
        Tipo_Documento:{}
        Nombre:{}
        Apellido:{}
        Email:{}
        Contraseña:{}
        Funciones:{}""".format(data[0],data[1],data[2]))

while True:
    print("==============================")
    print("/tCRUD")
    print("==============================")
    print("[1] Insertar registro")
    print("[2] Listar registro")
    print("[3] Actualizar registro")
    print("[4] Eliminar registro")
    print("[5] Buscar registro")
    print("[6] Salir")
    print("==============================")

    try:
        option=int(input("seleccionar una opcion:"))
        if (option ==1):
            create()
            time.sleep(1)
            system("clear")
        elif (option ==2):
            read()
        elif (option ==3):
            update()
            time.sleep(1)
            system("clear")
        elif (option ==4):
            delete()
            time.sleep(1)
            system("clear")
        elif (option ==5):
            search()           
        elif(option ==6):
            break
        else:
            print("opcio fuera de rango")
            time.sleep(1)
            system("clear")
    except:
        print("Error en elegir las opciones")
        