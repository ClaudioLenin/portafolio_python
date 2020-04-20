# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:17:59 2020

@author: claud
"""
"""Algoritmo de regresion lineal simple para predecir el precio de las casas 
en Boston de acuerdo al número de habitaciones"""

#LIBRERIAS A UTILIZAR
import numpy as np
from sklearn import  datasets,linear_model
import matplotlib.pyplot as plt
#Proporciona algoritmos de aprendizaje supervisado y no supervisado
#incluye numpy, pandas, matplotlib y mas


################# PREPARAR LA DATA #################
#Importamos los datos de la misma libreria de scikit-learn
boston = datasets.load_boston()
print(boston)
print()

################# ENTENDIMIENTO DE LA DATA #################
#Verifico la información contenida en el dataset
print("Información en el dataset: ")
print(boston.keys())
print()

#Verifico las caracteristicas del dataset
print("Caracteristicas del dataset: ")
print(boston.DESCR)
print()

#Verifico las caracteristicas del dataset
print("Cantidad de datos: ")
print(boston.data.shape)
print()

#Verifico la información de las columnas
print("Nombres columnas: ")
print(boston.feature_names)
print()

################# PREPARAR LA DATA REGRESIÓN LINEAL SIMPLE #################
#Seleccionamos solamente la columna 5 del dataset
X = boston.data[:,np.newaxis,5]

#Defino los datos correspondientes a las etiquetas
y = boston.target

#Graficamos los datos correspondientes
plt.scatter(X,y)
plt.xlabel("Número de habitantes")
plt.ylabel("Valor medio")
plt.show()

################# IMPLEMENTACION DE REGRESION LINEAL SIMPLE #################
from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#Defino el algoritmo a utilizar
lr = linear_model.LinearRegression()

#Entreno el modelo
lr.fit(X_train,y_train)

#Realizo una predicción
Y_pred = lr.predict(X_test)

#Graficamos los datos junto con el modelo
plt.scatter(X_test,y_test)
plt.plot(X_test,Y_pred,color = "red",linewidth=3)
plt.title("Regresión Lineal Simple")
plt.xlabel("Número de habitaciones")
plt.ylabel("Valor medio")
plt.show()

print()
print("DATOS DEL MODELO DE REGRESIÓN LINEAL SIMPLE")
print()
print("Valor de la pendiente o coeficiente 'a': ")
print(lr.coef_)
print("Valor de la intersección o coeficiente 'b': ")
print(lr.intercept_)
print()
print("La ecuación del modelo es igual a: ")
print("y = ",lr.coef_,"x = ",lr.intercept_)
print()
print("Precisión del modelo: ")
print(lr.score(X_train,y_train))

"""x_entrenamiento = variablesIndependientes_entrenamiento
y_entrenamiento = variablesDependientes_entrenamiento
x_prueba = variablesIndependientes_prueba
y_prueba = variablesDependientes_prueba

algoritmo = linear_model.LinearRegression()
algoritmo.fit(x_entrenamiento,y_entrenamiento)
algoritmo.predict(x_prueba)
a = algoritmo.coef_
b = algoritmo.intercept_
precision = algoritmo.score(x_prueba,y_prueba)
"""

