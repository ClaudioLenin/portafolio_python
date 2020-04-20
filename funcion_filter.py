# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:15:38 2020

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
        Empleado("Claudio","Director",800000),
        Empleado("Lili","Presidenta",700000),
        Empleado("Jany","Administrativa",600000),
        Empleado("Jos","Secretaria",500000),
        Empleado("Peter","Botones",100000)
        ]
salarios_altos = filter(lambda empleado:empleado.salario>500000,listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)

