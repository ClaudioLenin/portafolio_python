# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 07:38:27 2020

@author: claud
"""

#REGRESION LINEAL MULTIPLE
"""Desarrollo de una aplicacion para predecir el precio de las casas en boston 
de acuerdo al numero de habitaciones, el tiempo que ha tenido ocupada y la distancia
a la que se encuentra de los centros de trabajo de boston"""
from sklearn import datasets,linear_model

######################### PREPARAR LA DATA ################################
#Importamos los datos de la misma libreria de scikit-learn
bston = datasets.load_boston()
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

######################### PREPARAR LA DATA REGRESION LINEAL MULTIPLE ################################
#Seleccionamos las columnas 5,6 y 7 del dataset
X_multiple = boston.data[:,5:8]
print(X_multiple)

#Defino los datos correspondientes a las etiquetas
y_multiple = boston.target


######################### IMPLEMENTACION DE REGRESION LINEAL MULTIPLE ################################
from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train,X_test,y_train,y_test = train_test_split(X_multiple,y_multiple,test_size=0.2)

#Definimos el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

#Entreno el modelo
lr_multiple.fit(X_train,y_train)

#Realizo una prediccion
Y_pred_multiple = lr_multiple.predict(X_test)

print("DATOS DEL MODELO DE REGRESION LINEAL MULTIPLE")
print()

print('Valor de las pendientes o coeficientes "a":')
print(lr_multiple.coef_)

print('Valor de la interseccion o coeficientes "b":')
print(lr_multiple.intercept_)

print('Precisión del modelo:')
print(lr_multiple.score(X_train,y_train))



























