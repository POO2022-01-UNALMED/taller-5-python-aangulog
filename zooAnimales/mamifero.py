
# -*- coding: utf-8 -*-
from zooAnimales.animal import Animal

class Mamifero(Animal):
    totalMamiferos=0
    caballos=0
    leones=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.totalMamiferos+=1
        self.listado.append(self)
        
    @classmethod
    def cantidadMamiferos(cls): return cls.totalMamiferos
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos+=1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
        
    @classmethod
    def crearLeon(cls,nombre, edad, genero):
        cls.leones+=1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
        
    def isPelaje(self):
        return self._pelaje
    

    def setListado(self,a): self._listado=a
    def getListado(self): return self._listado
    def setPelaje(self,a): self._pelaje=a
    def getPelaje(self): return self._pelaje
    def setPatas(self,a): self._patas=a
    def getPatas(self): return self._patas