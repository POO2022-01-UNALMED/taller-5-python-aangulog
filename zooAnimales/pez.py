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

class Pez(Animal):
    totalPeces=0
    listado =[]
    salmones=0
    bacalaos=0
    
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.totalPeces+=1
        self.listado.append(self)
        
    @classmethod
    def cantidadPeces(cls): return cls.totalPeces 
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones+=1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
        
    @classmethod
    def crearBacalao(cls,nombre, edad, genero):
        cls.bacalaos+=1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def movimiento(self):
        return "nadar"
       
    def setColorEscamas(self,a): self._colorEscamas=a
    def getColorEscamas(self): return self._colorEscamas
    def setCantidadAletas(self,a): self._cantidadAletas=a
    def getCantidadAletas(self): return self._cantidadAletas