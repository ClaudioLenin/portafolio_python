# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:29:01 2020

@author: claud
"""
#REGRESION POLINOMIAL
"""Desarrollo de un modelo para predecir el precio de las casas en boston 
de acuerdo al numero de habitaciones"""

import numpy as np
from sklearn import datasets,linear_model
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
X_p = boston.data[:,np.newaxis,5]

#Defino los datos correspondientes a las etiquetas
y_p = boston.target

#Graficamos los datos correspondientes
plt.scatter(X_p,y_p)
plt.show()

######################### IMPLEMENTACION DE REGRESION POLINOMIAL ################################

from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train_p,X_test_p,y_train_p,y_test_p = train_test_split(X_p,y_p,test_size=0.2)

from sklearn.preprocessing import PolynomialFeatures

#Se define el grado del polinomio
poli_reg = PolynomialFeatures(degree = 2)

#Se transforma las caracteristicas existentes en caracteristicas de mayor grado
X_train_poli = poli_reg.fit_transform(X_train_p)
X_test_poli = poli_reg.fit_transform(X_test_p)

#Defino el algoritmo a utilizar
pr = linear_model.LinearRegression()

#Entreno el modelo
pr.fit(X_train_poli,y_train_p)

#Realizo una prediccion
Y_pred_pr = pr.predict(X_test_poli)

#Graficamos los datos junto con el modelo
plt.scatter(X_test_p,y_test_p)
plt.plot(X_test_p,Y_pred_pr,color="red",linewidth=3)
plt.show()

print()
print("DATOS DEL MODELO REGRESION POLINOMIAL")
print()

print("Valor de la pendiente o coeficiente 'a': ")
print(pr.coef_)

print("Valor de la interseccion o coeficiente 'b': ")
print(pr.intercept_)

print("Precisión del modelo: ")
print(pr.score(X_train_poli,y_train_p))