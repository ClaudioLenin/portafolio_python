# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:58:31 2023

@author: HP
"""

import numpy as np

#matriz vacias
unos = np.ones((3,4))
print(unos)

#matriz con valores 0
ceros = np.zeros((3,4))
print(ceros)

#matriz con valores aleatorios
aleatorios = np.random.random((2,2))
print(aleatorios)

#matriz vacía
vacia = np.empty((3,2))
print(vacia)

#matriz con un solo valor
full = np.full((2,2),8)
print(full)

#matriz con valores espaciados uniformemente
espacio1 = np.arange(0,30,5)
print(espacio1)
espacio2 = np.linspace(0,2,5)
print(espacio2)

#matriz identidad
identidad1 = np.eye(4,4)
print(identidad1)

identidad2 = np.identity(4)
print(identidad2)

#Conocer las dimensiones de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#Conocer el tipo de los datos
a = np.array([(1,2,3)])
print(a.dtype)

#Conocer el tamaño y forma de la matriz
a = np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)

#Cambio de forma de una matriz 
a = np.array([(8,9,10),(11,12,13)])
print(a)
a = a.reshape(3,2)
print(a)

#Extraer un solo valor de la matriz - el valor ubicado en la fila 0 columna 2
a = np.array([(1,2,3,4),(3,4,5,6)])
print(a[0,2])

#Extraer los valores de todas las filas ubicadas en la columna 3
a = np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,2])

#Encontrar el mínimo, máximo y la suma
a = np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())

#Encontrar la raíz cuadrada y la desviación estándar
a = np.array([(1,2,3),(3,4,5)])
print(np.sqrt(a))
print(np.std(a))

#Calcular la suma, resta, multiplicacion y division de 2 matrices
x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)