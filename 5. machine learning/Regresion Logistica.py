# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 07:52:14 2020

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

######################### IMPLEMENTACION DE REGRESION LOGISTICA ################################
from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#Se escalan todos los datos 
from sklearn.preprocessing import StandardScaler
escalar = StandardScaler()
X_train = escalar.fit_transform(X_train)
X_test = escalar.transform(X_test)

#Defino el algoritmo a utilizar
from sklearn.linear_model import LogisticRegression
algoritmo = LogisticRegression()

#Entreno el modelo
algoritmo.fit(X_train,y_train)

#Realizo una prediccion
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

#Calculo de la exactitud del modelo
from sklearn.metrics import accuracy_score
exactitud = accuracy_score(y_test,y_pred)
print("Calculo de la exactitud del modelo:")
print(exactitud)

#Calculo de la sensibilidad del modelo
from sklearn.metrics import recall_score
sensibilidad = recall_score(y_test,y_pred)
print("Calculo de la sensibilidad del modelo:")
print(sensibilidad)

#Calculo el puntaje F1 del modelo
from sklearn.metrics import f1_score
puntaje = f1_score(y_test,y_pred)
print("Calculo el puntaje F1 del modelo:")
print(puntaje)

#Calculo de la curva ROC - AUC del modelo
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_test,y_pred)
print("Calculo el puntaje F1 del modelo:")
print(roc_auc)
