
class Habitacion:
    def __init__(self, num_habitacion, tipo_habitacion, precio_habitacion, estado_habitacion):
        self.__num_habitacion=num_habitacion
        self.tipo_habitacion=tipo_habitacion
        self.precio_habitacion=precio_habitacion
        self.estado_habitacion=estado_habitacion
        
    def getNum(self):
        return self.__num_habitacion
    
    def setNum(self,num_habitacion):
        self.__num_habitacion=num_habitacion
    
    def getTipo(self):
        return self.tipo_habitacion
    
    def setTipo(self, tipo_habitacion):
        self.tipo_habitacion=tipo_habitacion
        
    def getPrecio(self):
        return self.precio_habitacion
    
    def setPrecio(self, precio_habitacion):
        self.precio_habitacion=precio_habitacion
        
    def getEstado(self):
        return self.estado_habitacion
    
    def setEstado(self, estado_habitacion):
        self.estado_habitacion=estado_habitacion