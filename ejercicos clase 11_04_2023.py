# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:39:09 2023

@author: lab
"""
"""Explicacion de for y listas"""

# lista = ["r1","S1","r2","ap10",1]
# for item in lista:
#     print(lista)
    
# print("\n"*2)
    
# lista = ["r1","S1","r2","ap10",1]
# for item in lista:
#     print(item)
     
# print("\n"*2)


# for i in range(1,10+1,1):
#     print(i)


# tex = " una vez salesionado x siempre salesiano"

# for puntero in tex:
#     print(puntero)
    
# print("\n"*2)

# for puntero in tex:
#     print(puntero, end="")
    
# print("\n"*2)
    
# for puntero in tex:
#     print(tex)
    
# print("\n"*2)
    
tex = " una vez salesionado x siempre salesiano"

for puntero in tex:
    if "s" in puntero:
        
        
        print(puntero)
    






# for a in range (10,1,-2):
#     print(a)
    
  
# devices = ["r1","r2","r5","e4","w3","g4"]

# for a in devices:
#     print(a)
    
# rout = []
# swit = []
# devices = ["R1","R2","R3","S1","S2","AP1"]

# for a in devices:
#     if "R" in a:
#         rout.append(a)
#     else:
#         swit.append(a)
# print(swit)
# print(rout)

a = []
o = []
s = []
varios= []

tex = " una vez salesionado x siempre salesiano"

for puntero in tex:
    if "s" in puntero:
        s.append(puntero)
        
    elif "a" in puntero:
        a.append(puntero)
        
    elif "o" in puntero:
        o.append(puntero)
        
    else:
        varios.append(puntero)
    
print(a)
print(o)      
print(s)
print(varios)
      
    