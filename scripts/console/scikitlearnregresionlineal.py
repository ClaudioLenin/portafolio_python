import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
#   Definir algoritmo
#linear_model.LinearRegression()
#   Entrenar modelo
#fit(x,y)
#   Predecir modelo
#predict(x)
#   Conocer pendiente (a)
#coef_
#   Conocer intersección (b)
#intercept_
#   Precisión modelo
#score(x)
################## PREPARAR LA DATA ##################
boston = datasets.load_boston()
print(boston)
print()
################## ENTENDIMIENTO DE LA DATA ##################
#Verifico la información contenida en el dataset
print('Información en el dataset:')
print(boston.keys())
print()