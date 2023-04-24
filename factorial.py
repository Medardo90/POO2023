# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:31:25 2023

@author: lab
"""

def fac(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*fac(n-1)
   return resultado
fac5=fac(5)


