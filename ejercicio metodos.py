# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""Funciones en python son 
modulos:son archivos echos en python
si entendemos funciones son iguales a metodos 
"""
# def mensaje():
#     print("preciona el siguiente valor")
    
# print("nosotros estampos aqui")

# print("precionameos aqui")
# mensaje()

# función con un parámetro
# def holaConNombre(name):
#   print("Hello ",name,"!")

# holaConNombre("Patricio")  # llamada a la función, 'Hello Ada!' se muestra en la consola

# ###############################################
# def dirrecion(calle, ciudad, barrio):
#     print("Su pedido va ala ciudad : ",ciudad)
    
#     print("Su domicilio esta en la calle : ",barrio)
    
#     print("se refencia cen la calle como  : ",ciudad)
    
# ci = input("ingrese la ciudad:")
# ba = input("ingrese el barrio: ")
# ca = input("ingrese la calle: ")

# dirrecion(ci, ci, ba)

#############################################

# def resta(num1, num2):
#     print("la resta de: ", num1,"-", num2, "es:", num1-num2)
    
# resta(8,6)
# resta(num1=56, num2 =4)
# resta(5,num2 = 2)

#################################################

# def multiplicacion(numero1, numero2):
#     print(numero1 * numero2)
#     return()

# resultado = multiplicacion(5,2)
# total = resultado + 1
    
########################################################
    
# def holatodos(lista):
#     for item in lista :
#         print("hola", lista)
        
# holatodos(["juan"])
# holatodos(["juan","ana"])

#############################################

# def crearlista(numero):
#     lista = []
#     for item in range(1, numero+1,1):
#         lista.append(item)
#         return lista
# print(crearlista(10))

####################################

def suma(*a):
    print("\nTipo de datos del argumento:",
         type(a))
    sum = 0
    for n in a:
        sum +=n
        #sum=sum+n

    print("Suma:",sum)

suma(0,1)
suma(1,2)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)
suma(1,2,3,5,6,7,8,9,10)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17)

###########################################

def keyw(**datos):
    print("\nTipo de datos del argumento:",
          type(datos))

    for key, value in datos.items():
        print("{} is {}".format(key,value))

keyw(Firstname="Juan", 
     Lastname="Domínguez", 
     Age=42, 
     Phone=1234567890)
keyw(Firstname="John", 
     Lastname="Wood",
     Email="johnwood@nomail.com",
     Country="Wakanda", 
     Age=25, 
     Phone=9876543210)




































