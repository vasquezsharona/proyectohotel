
class cliente:
    def __init__(self,Num_doc,Tipo_doc,Nombres,Apellidos,Correo,Contraseña):
        self.__Num_doc=Num_doc
        self.__Tipo_doc=Tipo_doc
        self.__Nombres=Nombres
        self.__Apellidos=Apellidos
        self.__Correo=Correo
        self.__Contraseña=Contraseña

    def getNum_doc(self):
          return self.__Num_doc

    def setNum_doc(self,Num_doc):
          self.__Num_doc=Num_doc   

    def getTipo_doc(self):
          return self.__Tipo_doc

    def setTipo_doc(self,Tipo_doc):
          self.__Tipo_doc=Tipo_doc    

    def getNombres(self):
          return self.__Nombres

    def setNombres(self,Nombres):
          self.__Nombres=Nombres

    def getApellidos(self):
          return self.__Apellidos

    def setApellidos(self,Apellidos):
          self.__Apellidos=Apellidos

    def getCorreo(self):
          return self.__Correo

    def setCorreo(self,Correo):
          self.__Correo=Correo

    def getContraseña(self):
          return self.__Contraseña

    def setContraseña(self,Contraseña):
          self.__Contraseña=Contraseña