# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:52:12 2020

@author: claud
"""

import numpy as np
import sys
import time

#-------------------------------MATRIZ VACIA---------------------------------
"""Se lo puede llenar despues de haber creado"""
print("MATRIZ VACIA")
vacia = np.empty((3,2))
print(vacia)

#-------------------------------MATRIZ CON TODOS LOS VALORES 0---------------------------------
print("MATRIZ CON TODOS LOS VALORES 0")
ceros = np.zeros((3,4))
print(ceros)

#-------------------------------MATRIZ CON TODOS LOS VALORES 1---------------------------------
print("MATRIZ CON TODOS LOS VALORES 1")
unos = np.ones((3,4))
print(unos)

#-------------------------------MATRIZ CON UN SOLO VALOR---------------------------------
print("MATRIZ CON UN SOLO VALOR")
full = np.full((3,4),8)
print(full)

#-------------------------------MATRIZ CON TODOS LOS VALORES ALEATORIOS---------------------------------
print("MATRIZ CON TODOS LOS VALORES ALEATORIOS")
aleatorios = np.random.random((2,2))
print(aleatorios)

#-------------------------------MATRIZ CON VALORES ESPACIADOS UNIFORMEMENTE---------------------------------
print("MATRIZ CON VALORES ESPACIADOS UNIFORMEMENTE")
espacio1 = np.arange(0,30,5)
print(espacio1)

espacio2 = np.linspace(0,2,5)
print(espacio2)

#-------------------------------MATRIZ IDENTIDAD---------------------------------
print("MATRIZ IDENTIDAD")
identidad1 = np.eye(4,4)
print(identidad1)

identidad2 = np.identity(4)
print(identidad2)

#-------------------------------MATRIZ 1D---------------------------------
a = np.array([1,2,3]) #Ocupa menos memoria que las listas de python
print('MATRIZ 1D')
print(a)
print()

#-------------------------------MATRIZ 2D---------------------------------
b = np.array([(1,2,3),(4,5,6)]) #Ocupa menos memoria que las listas de python
print('MATRIZ 2D')
print(b)
print()

#-------------------------------CONOCER LAS DIMENSIONES DE UNA MATRIZ---------------------------------
print("CONOCER LAS DIMENSIONES DE UNA MATRIZ")
a = np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print(a.ndim)

print("CONOCER EL TIPO DE DATOS DE LA MATRIZ")
print(a.dtype)

print("CONOCER EL TAMAÑO DE LA MATRIZ")
print(a.size)

print("CONOCER LA FORMA DE LA MATRIZ")
print(a.shape)

print("TOMAR UN VALOR DE LA MATRIZ")
print(a[0,2])

print("TOMAR LOS VALORES DE TODAS LAS FILAS UBICADAS EN LA COLUMNA 3")
print(a[0:,2])

print("TRANSFORMAR LA MATRIZ")
a = a.reshape(4,2)
print(a)
print()

print("ENCONTRAR EL MINIMO, MAXIMO Y LA SUMA")
print(a.min())
print(a.max())
print(a.sum())
print()

print("ENCONTRAR LA RAIZ CUADRADA Y LA DESVIACION ESTANDAR")
print(np.sqrt(a))
print(np.std(a))
print()

print("+, -, *, / DE DOS MATRICES")
x = np.array([(1,2,3),(4,5,6)])
y = np.array([(1,2,3),(4,5,6)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print()

#-------------------------------Evaluar Memoria asignada---------------------------------
print("EVALUAR MEMORIA ASIGNADA")
S = range(1000)
print("Resultado lista Python:")
print(sys.getsizeof(5)*len(S),"Memoria asignada")
print()

D = np.arange(1000)
print("Resultado NumPy array:")
print(D.size*D.itemsize,"Memoria asignada")
print()

#-------------------------------Evaluar Rapidez---------------------------------
print("EVALUAR RAPIDEZ")
SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]

print("Resultado lista de Python:")
print((time.time()-start)*1000)
print()

start = time.time()
result = A1+A2
print("Resultado NumPy array:")
print((time.time()-start)*1000)
print()