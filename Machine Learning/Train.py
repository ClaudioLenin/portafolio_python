# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:12:56 2020

@author: claud
"""
import pandas as pd
import numpy as np

df = pd.read_csv('train.csv') #Importar datos

print(df)

#------------------------------VERIFICAR DATOS NULOS EN EL DATAFRAME----------------------------------
print("VERIFICAR DATOS NULOS EN EL DATAFRAME")
print(df.isnull())

#------------------------------SUMA DE DATOS NULOS EN EL DATAFRAME----------------------------------
print("SUMA DE DATOS NULOS EN EL DATAFRAME")
print(df.isnull().sum())

#------------------------------REEMPLAZAR LOS DATOS PERDIDOS POR LA MEDIA----------------------------------
print("REEMPLAZAR LOS DATOS PERDIDOS POR LA MEDIA")
print(df.fillna(df.mean()))