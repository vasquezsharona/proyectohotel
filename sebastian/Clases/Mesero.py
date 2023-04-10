
class Mesero:
    def __init__(self,Num_documento,Tipo_documento,Nombres,Apellidos,Email,Contraseña,Funciones):
        self.__Num_documento=Num_documento
        self.__Tipo_documento=Tipo_documento
        self.__Nombres=Nombres
        self.__Apellidos=Apellidos
        self.__Email=Email
        self.__Contraseña=Contraseña
        self.__Funciones=Funciones

    def getNum_documento(self):
          return self.__Num_documento

    def setNum_documento(self,Num_documento):
          self.__Num_documento=Num_documento   

    def getTipo_documento(self):
          return self.__Tipo_documento

    def setTipo_documento(self,Tipo_documento):
          self.__Tipo_documento=Tipo_documento    

    def getNombres(self):
          return self.__Nombres

    def setNombres(self,Nombres):
          self.__Nombres=Nombres

    def getApellidos(self):
          return self.__Apellidos

    def setApellidos(self,Apellidos):
          self.__Apellidos=Apellidos

    def getEmail(self):
          return self.__Email

    def setEmail(self,Email):
          self.__Email=Email

    def getContraseña(self):
          return self.__Contraseña

    def setContraseña(self,Contraseña):
          self.__Contraseña=Contraseña

    def getFunciones(self):
          return self.__Funciones

    def setFunciones(self,Funciones):
          self.__Funciones=Funciones




''' Actualizar_servicio Eliminar_servicio")
print("el mesero: ",mesero1.getNombres(),mesero1.getApellidos())
print("que tiene: ",mesero1.getTipo_doc())
print("con el numero: ",mesero1.getNum_doc())
print("cuyas funciones son : ",mesero1.getFunciones())'''