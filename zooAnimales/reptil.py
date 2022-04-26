# -*- coding: utf-8 -*-
def setget(listOfNames):
    for name in listOfNames:
        print("    def set"+name.capitalize()+"(self,a): self._"+name+"=a"+"\n    def get"+name.capitalize()+"(self): return self._"+name)
def inau(ListOfAtrib):
    print("def __init__(self,nombre,edad,habitat,genero,zona" , *ListOfAtrib,sep=",",end="")
    print("):")
    print("        super().__init__(self, nombre, edad, habitat, genero, zona)")
    for atrib in ListOfAtrib:
        print("        self._"+atrib+" = "+atrib)
    print("")
    setget(ListOfAtrib)
    print("        self.total_+=1")
    print("        self.listado.append(self)")
from zooAnimales.animal import Animal

class Reptil(Animal):
    totalReptiles=0
    listado =[]
    serpientes=0
    iguanas=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.totalReptiles+=1
        self.listado.append(self)
        
    @classmethod
    def cantidadReptiles(cls): return cls.totalReptiles 
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas+=1
        return Reptil(nombre, edad, "humdeal", genero, "verde", 3)
        
    @classmethod
    def crearSerpiente(cls,nombre, edad, genero):
        cls.serpientes+=1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    def movimiento(self):
        return "reptar"

    def setColorEscamas(self,a): self._colorEscamas=a
    def getColorEscamas(self): return self._colorEscamas
    def setLargoCola(self, a): self._largoCola = a
    def getLargoCola(self): return self._largoCola