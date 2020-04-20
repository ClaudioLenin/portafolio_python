# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:58:09 2020

@author: claud
"""

"""Desarrollo de un modelo para predecir si una persona tiene cancer de seno o 
no de acuerdo a las caracteristicas del tumor"""

from sklearn import datasets

######################### PREPARAR LA DATA ################################
#Importamos los datos de la misma libreria de scikit-learn
dataset = datasets.load_breast_cancer()
print(dataset)
print()

######################### ENTENDIMIENTO DE LA DATA ################################
#Verifico la información contenida en el dataset
print("Información en el dataset: ")
print(dataset.keys())
print()

#Verifico las caracteristicas del dataset
print("Caracteristicas del dataset: ")
print(dataset.DESCR)
print()

#Verifico la cantidad de datos que hay en los dataset
print("Cantidad de datos: ")
print(dataset.data.shape)
print()

#Verifico la información de las columnas
print("Nombres columnas: ")
print(dataset.feature_names)
print()

######################### SELECCIONAMOS TODAS LAS COLUMNAS ################################
X = dataset.data

#Defino los datos correspondientes a las etiquetas
y = dataset.target

######################### IMPLEMENTACION DE ARBOL DECISION CLASIFICACION ################################
from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#Defino el algoritmo a utilizar Arbol de decision clasificacion
from sklearn.tree import DecisionTreeClassifier

algoritmo = DecisionTreeClassifier(criterion='entropy')

#Entreno el modelo
algoritmo.fit(X_train,y_train)

#Realizo una perdiccion
y_pred = algoritmo.predict(X_test)

#------------------------------------------------------------------------------
#Verifico la matriz de Confusión
from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(y_test,y_pred)
print("Matriz de confusion: ")
print(matriz)

#Calculo de precision del modelo 
from sklearn.metrics import precision_score
precision = precision_score(y_test,y_pred)
print("Calculo de precision del modelo:")
print(precision)