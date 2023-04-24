# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

print("Bienvenido a la liga - formato de registo")
dato=input("ingrese su nombre: ")
dato1=input("ingrese su apellido: ")
dato2=int(input("ingrese su edad: "))
dato3=int(input("ingrese su estatura: "))
dato4=int(input("ingrese su peso en kg: "))
dato5=input("disciplina a la que pertenece: ")

if dato2 >=5 and dato2 <=7:
    print("Esta en la categoria infantil")
elif dato2 >=8 and dato2 <=15:
    print("Esta en la categoria juvenil")
elif dato2 >=16 and dato2 <=18:
    print("Esta en la categoria amateur")
elif dato2 >=19 and dato2 <=30:
    print("Esta en la categoria profesional")
elif dato2 >=31 and dato2 <=40:
    print("Esta en la categoria profesopnal AM")
else:
    print("Lo sentimos, no ingresa en ninguna categoria")