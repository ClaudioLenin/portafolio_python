# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:04:03 2020

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

######################### PREPARAR LA DATA REGRESION POLINOMIAL ################################
#Seleccionamos solamente la columna 6 del dataset
X_svr = boston.data[:,np.newaxis,5]

#Defino los datos correspondientes a las etiquetas
y_svr = boston.target

#Graficamos los datos correspondientes
plt.scatter(X_svr,y_svr)
plt.show()

######################### IMPLEMENTACION DE VECTORES DE SOPORTE REGRESION ################################

from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train,X_test,y_train,y_test = train_test_split(X_svr,y_svr,test_size=0.2)

from sklearn.svm import SVR

#Defino el algoritmo a utilizar
svr = SVR(kernel='linear',C=1.0,epsilon=0.2)

#Entreno el modelo
svr.fit(X_train,y_train)

#Realizo una prediccion
Y_pred = svr.predict(X_test)

#Graficamos los datos junto con el modelo
plt.scatter(X_test,y_test)
plt.plot(X_test,Y_pred,color='red',linewidth=3)
plt.show()

print()
print("DATOS DEL MODELO VECTORES DE SOPORTE REGRESION")
print()

print("Precision del modelo:")
print(svr.score(X_train,y_train))


