# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:17:30 2023

@author: lab
"""

class arbol:
    def __init__(self,tipo,edad,tamaño, altura,forma):
        self.tipo=tipo
        self.edad=edad
        self.tamaño=tamaño
        self.altura=altura
        self.forma=forma
    def crecer(self):
        print("crecimiento del arbol")
    def fotosintesis(self):
        print("")
    def dar_sombra(self):
        print("")
    def respirar(self):
        print("")
    def morir(self):
       print("")  
amanzana=arbol("tipo", "edad","tamaño", "altura","forma")       
amanzana.crecer()
amanzana.fotosintesis()
amanzana.dar_sombra()
amanzana.respirar()
