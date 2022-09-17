# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:24:50 2020

@author: claud
"""
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)
    

listaEmpleados = [
        Empleado("Claudio","Director",6700),
        Empleado("Lili","Presidenta",7500),
        Empleado("Jany","Administrativa",2100),
        Empleado("Jos","Secretaria",2150),
        Empleado("Peter","Botones",1800)
        ]
def calculo_comision(empleado):
    
    if(empleado.salario<=3000):
        
        empleado.salario = empleado.salario*1.03
    
    return empleado

listaEmpleadosComision = map(calculo_comision,listaEmpleados) #Aplica un porcentaje de aumento a cada elemento

for empleado in listaEmpleadosComision:
    print(empleado)