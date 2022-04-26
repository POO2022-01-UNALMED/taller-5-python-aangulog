# -*- coding: utf-8 -*-

from zooAnimales.animal import Animal

class Anfibio(Animal):
    totalAnfibios=0
    listado =[]
    ranas=0
    salamandras=0
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.totalAnfibios+=1
        self.listado.append(self)
        
    @classmethod
    def cantidadAnfibios(cls): return cls.totalAnfibios
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas+=1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
        
    @classmethod
    def crearSalamandra(cls,nombre, edad, genero):
        cls.salamandras+=1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    def movimiento(self):
        return "saltar"
        
    def isVenenoso(self):
        return self._venenoso
    
    def setColorPiel(self,a): self._colorPiel=a
    def getColorPiel(self): return self._colorPiel
    def setVenenoso(self,a): self._venenoso=a
    def getVenenoso(self): return self._venenoso