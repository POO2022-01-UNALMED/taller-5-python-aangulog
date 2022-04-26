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
from zooAnimales.animal import Animal

class Ave(Animal):
    totalAves=0
    listado =[]
    halcones=0
    aguilas=0
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.totalAves+=1
        self.listado.append(self)
        
    @classmethod
    def cantidadAves(cls): return cls.totalAves
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones+=1
        return Ave(nombre, edad, "montañas", genero,"cafe glorioso")
        
    @classmethod
    def crearAguila(cls,nombre, edad, genero):
        cls.aguilas+=1
        return Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
        
    def movimiento(self):
        return "volar"
        
    def setColorPlumas(self,a): self._colorPlumas=a
    def getColorPlumas(self): return self._colorPlumas