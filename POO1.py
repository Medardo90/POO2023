# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:46:18 2023

@author: lab
"""

class Employee:
    empCount=0
    def __init__(self,name, salary):
       self.name=name
       self.salary=salary
       Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d", Employee.empCount)
          
    def displayEmployee(self):
        print("Name: ",self.name, ",Salary: ",self.salary)
   
empleado1=Employee("Juan Martinez", 800)
empleado2=Employee("Sandra", 900)
empleado1.displayEmployee()
print("Total Employee %d" % Employee.empCount)

