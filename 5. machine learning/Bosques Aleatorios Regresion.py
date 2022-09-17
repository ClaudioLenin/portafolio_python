# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:54:19 2020

@author: claud
"""

"""Modelo para predecir el precio de las habitaciones de Boston de acuerdo
a la cantidad de habitaciones"""

import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

######################### PREPARAR LA DATA ################################
#Importamos los datos de la misma libreria de scikit-learn
boston = datasets.load_boston()
print(boston)
print()

######################### ENTENDIMIENTO DE LA DATA ################################
#Verifico la información contenida en el dataset
print("Información en el dataset: ")
print(boston.keys())
print()

#Verifico las caracteristicas del dataset
print("Caracteristicas del dataset: ")
print(boston.DESCR)
print()

#Verifico la cantidad de datos que hay en los dataset
print("Cantidad de datos: ")
print(boston.data.shape)
print()

#Verifico la información de las columnas
print("Nombres columnas: ")
print(boston.feature_names)
print()

######################### PREPARAR LA DATA BOSQUES ALEATORIOS REGRESION ################################
#Seleccionamos solamente la columna 6 del dataset
X_bar = boston.data[:,np.newaxis,5]

#Defino los datos correspondientes a las etiquetas
y_bar = boston.target

#Graficamos los datos correspondientes
plt.scatter(X_bar,y_bar)
plt.show()

######################### IMPLEMENTACION DE ARBOLES DE DECISION REGRESION ################################

from sklearn.model_selection import train_test_split



#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train,X_test,y_train,y_test = train_test_split(X_bar,y_bar,test_size=0.2)

from sklearn.ensemble import RandomForestRegressor

#Defino el algoritmo a utilizar
bar = RandomForestRegressor(n_estimators=300, max_depth = 8)

#Entreno el modelo
bar.fit(X_train,y_train)

#Realizo una prediccion
Y_pred = bar.predict(X_test)

#Graficamos los datos junto con el modelo
X_grid = np.arange(min(X_test),max(X_test),0.1) #Para espaciar los datos en 0.1
X_grid = X_grid.reshape((len(X_grid),1)) #dar una nueva forma a la matriz de datos
plt.scatter(X_test,y_test)
plt.plot(X_grid,bar.predict(X_grid),color='red',linewidth=3)
plt.show()

print()
print("DATOS DEL MODELO VECTORES DE SOPORTE REGRESION")
print()

print("Precision del modelo:")
print(bar.score(X_train,y_train))
