# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:58:47 2020

@author: claud
"""

import random

intentosRealizados = 0

print('{} como {}'.format('¿Hola','te llamas?'))

miNombre = input()

numero = random.randint(1,20)
print('Bueno, '+miNombre+' estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar: ')
    estimacion = input()
    estimacion = int(estimacion)
    
    intentosRealizados = intentosRealizados+1
    
    if estimacion < numero:
        print('Tu estimacion es muy baja. ')
    
    if estimacion > numero:
        print('Tu estimacion es muy alta. ')    
        
    if estimacion == numero:
        break
    
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, '+miNombre+'! ¡Hás adivinado mi número en '+ intentosRealizados + ' intentos!')
    
if estimacion != numero:
    numero = str(numero)
    print('Pues no. El número que estaba pensando era: '+numero)