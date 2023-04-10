class tb_cliente:
    def __init__(self,id_cliente,id_habitacion,nombre,apellido,correo_electronico,telefono,direccion):
        self._id_cliente = id_cliente
        self._id_habitacion = id_habitacion
        self._nombre = nombre
        self._apellido = apellido
        self._correo_electronico = correo_electronico
        self._telefono = telefono
        self._direcciion = direccion

        def getcliente(self):
            return self.__id_cliente, self.id_habitacion, self.nombre, self.apellido, self.correo_electronico, self.telefono, self.direccion
        
        def setid_cliente(self,id_cliente):
            self. id_cliente = id_cliente
