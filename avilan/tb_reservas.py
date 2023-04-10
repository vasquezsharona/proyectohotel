class tb_reservas:
    def __init__(self,id_reservas,id_cliente,id_habitacion,fecha_entrada,fecha_salida,cantidad_personas,total_reservas):
        self._id_cliente = id_cliente
        self._id_habitacion = id_habitacion
        self._id_reservas = id_reservas
        self._fecha_entrada = fecha_entrada
        self._fecha_salida = fecha_salida
        self._cantidad_personas = cantidad_personas
        self._total_reservas = total_reservas

        def getreservas(self):
            return self.__id_reservas,id_cliente, self.id_habitacion, self.fecha_entrada, self.fecha_salida, self.cantidad_personas, self.total_reservas
        
       
        def setid_reservas(self,id_reservas):
            self. id_reservas = id_reservas
           
        def setid_cliente(self,id_cliente):
            self. id_cliente = id_cliente

        def setid_habitacion(self,id_habitacion):
            self. id_habitacion = id_habitacion

        def setfecha_entrada(self,fecha_entrada):
            self. fecha_entrada = fecha_entrada

        def setfecha_salida(self,fecha_salida):
            self. fecha_salida = fecha_salida

        def setcantidad_personas(self,cantidad_personas):
            self. cantidad_personas = cantidad_personas
        
        def setTotal_reservas(self,total_reservas):
            self. total_reservas = total_reservas

          
    

