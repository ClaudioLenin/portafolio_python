# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:15:26 2023

@author: HP
"""

import numpy as np
import pandas as pd

data = np.array([['','col1','col2'],['Fila1',11,22],['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print('DataFrame:')
print(df)

series = pd.Series({"Argentina":"Buenos Aires",
                    "Chile":"Santiago de Chile",
                    "Colombia":"Bogotá",
                    "Perú":"Lima"})
print("Series:")
print(series)

#Forma del DataFrame
print('Forma del DataFrame:')
print(df.shape)

#Altura del DataFrame
print('Altura del DataFrame:')
print(len(df.index))

#Estadísticas del DataFrame
print("Estadísticas del DataFrame:")
print(df.describe())

#Media de las columnas DataFrame
print('Media de las columnas DataFrame:')
print(df.mean())

#Correlación del DataFrame
print('Correlación del DataFrame:')
print(df.corr())

#Cuenta los datos del DataFrame
print('Cuenta los datos del DataFrame:')
print(df.count())

#Valor más alto de cada columna del DataFrame
print('Valor más alto de cada columna del DataFrame:')
print(df.max())

#Valor más bajo de cada columna del DataFrame
print('Valor más bajo de cada columna del DataFrame:')
print(df.min())

#Mediana de cada columna del DataFrame
print('Mediana de cada columna del DataFrame:')
print(df.median())

#Desviación estándar de cada columna del DataFrame
print('Desviación estándar de cada columna del DataFrame:')
print(df.std())

#Seleccionar la primera columna del DataFrame
print('Primera columna del DataFrame:')
print(df[0])

#Seleccionar 2 columnas del DataFrame
print('Primera 2 columnas del DataFrame:')
print(df[[0,1]])

#Seleccionar el valor de la primera fila y la última columna del DataFrame
print('Valor de la primera fila y la última columna del DataFrame:')
print(df.iloc[0][2])

#Seleccionar los valores de la primera fila del DataFrame
print('Valores de la primera fila del DataFrame:')
print(df.loc[0])

#Seleccionar los valores de la primera fila del DataFrame
print('Valores de la primera fila del DataFrame:')
print(df.iloc[0,:])

#Importar datos csv
#df = pd.read_csv('train.csv')

#Verificar si hay datos nulos en el DataFrame
print('Datos nulos en el DataFrame:')
print(df.isnull())

#Suma de datos nulos en el DataFrame
print('Suma de datos nulos en el DataFrame:')
print(df.isnull().sum())
#Para eliminar datos perdidos
#pd.dropna()
#df.dropna(axis=1)

#Reemplazar los valores perdidos por la media
print('Reemplazar los valores perdidos por la media:')
print(df.fillna(df.mean()))

