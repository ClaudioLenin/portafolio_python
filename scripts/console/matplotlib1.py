# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:43:35 2023

@author: HP
"""

import matplotlib.pyplot as plt

#Los datos deben estar estructurados por numpy

a = [1,2,3,4]
b = [11,22,33,44]

plt.plot(a,b,color='blue',linewidth=3,label='línea')
plt.legend()
plt.show()

#algunos modulos de matplotlib:
#pyplot
#pylab (obsoleto)