# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:46:49 2023

@author: HP
"""

import sys
import numpy as np
import time

#Array de 1 y 2 dimensiones
a = np.array([1,2,3])
print('1D array:')
print(a)
print()

b = np.array([(1,2,3),(4,5,6)])
print('2D array:')
print(b)

#Comparacion de uso de memoria de un array hecha por sys otra por numpy
S = range(1000)
print('Resultado lista de Python:')
print(sys.getsizeof(5)*len(S))
print()
D = np.arange(1000)
print('Resultado NumPy array:')
print(D.size*D.itemsize)

#Comparacion de uso de rapidez
SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print('Resultado lista de Python:')
print((time.time() - start) * 1000)
print()
start = time.time()
result = A1 + A2
print('Resultado NumPy array:')
print((time.time() - start) * 1000)