

# from gestion.zoologico import Zoologico 


class Zona:
    def __init__(self,nombre,zoo=None,animales=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales
    
    # def __init__(self,nombre):
    #     self._nombre = nombre
    

    def setNombre(self,a): self._nombre=a
    def getNombre(self): return self._nombre
    def setZoo(self,a): self._zoo=a
    def getZoo(self): return self._zoo
    def setAnimales(self,a): self._animales=a
    def getAnimales(self): return self._animales
    
    def agregarAnimales(self,animal):
        if self._animales is None:
            self._animales=[]
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        if self._animales is None:
            return 0
        else:
            return len(self._animales)

        