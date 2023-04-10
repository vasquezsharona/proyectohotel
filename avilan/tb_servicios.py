class tb_servicios:
    def __init__(self,id_servicio,nombre,descripcion,cantidad,precio_unitario):
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._precio_unitario = precio_unitario

        def getcliente(self):
            return self.__id_servicio, self.nombre, self.descripcion, self.cantidad, self.precio_unitario
        
        def setid_servicio(self,id_servicio):
            self. id_servicio = id_servicio

        def setnombre(self,nombre):
            self. nombre = nombre

        def setdescripcion(self,descripcion):
            self. descripcion = descripcion   

        def setcantidad(self,cantidad):
            self. cantidad = cantidad

        def setprecio_unitario(self,precio_unitario):
            self. precio_unitario = precio_unitario
        
        
