
# from gestion.zona import Zona


class Zoologico:
    def __init__(self, nombre, ubicacion, zonas=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas #Lista
        
    def agregarZonas(self,zona):
        if self._zonas is None:
            self._zonas=[]
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self):
        counter=0
        for zona in self._zonas:
            counter+=zona.cantidadAnimales()
        # return int(counter/2)
        return counter
            
        
    def setZona(self,a): self._zonas=a
    def getZona(self): return self._zonas
    def setUbicacion(self,a): self._ubicacion=a
    def getUbicacion(self): return self._ubicacion
    def setNombre(self,a): self._nombre=a
    def getNombre(self): return self._nombre