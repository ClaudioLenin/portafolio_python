# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:09:13 2020

@author: claud
"""

import pandas as pd
import numpy as np

#-----------------------------------DATAFRAME----------------------------------
data = np.array([['','Col1','Col2'],['Fila1',11,22],['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print("DataFrame:")
print(df)

#-----------------------------------FORMA DE UN DATAFRAME----------------------------------
print("FORMA DE UN DATAFRAME")
print(df.shape)

#-----------------------------------ALTURA DE UN DATAFRAME----------------------------------
print("ALTURA DE UN DATAFRAME")
print(len(df.index))

#-----------------------------------ESTADÍSTICAS DEL DATAFRAME----------------------------------
print("ESTADÍSTICAS DEL DATAFRAME")
print(df.describe())

#-----------------------------------MEDIA DE LAS COLUMNAS DEL DATAFRAME----------------------------------
print("MEDIA DE LAS COLUMNAS DEL DATAFRAME")
print(df.mean())

#-----------------------------------MEDIANA DE LAS COLUMNAS DEL DATAFRAME----------------------------------
print("MEDIANA DE LAS COLUMNAS DEL DATAFRAME")
print(df.median())

#-----------------------------------DESVIACIÓN ESTANDAR DE LAS COLUMNAS DEL DATAFRAME----------------------------------
print("DESVIACIÓN ESTANDAR DE LAS COLUMNAS DEL DATAFRAME")
print(df.std())

#-----------------------------------CORRELACIÓN DEL DATAFRAME----------------------------------
print("CORRELACIÓN DEL DATAFRAME")
print(df.corr())

#-----------------------------------CUENTA LOS DATOS DEL DATAFRAME----------------------------------
print("CUENTA LOS DATOS DEL DATAFRAME")
print(df.count())

#-----------------------------------VALOR MAS ALTO DE UNA COLUMNA DEL DATAFRAME----------------------------------
print("VALOR MAS ALTO DE UNA COLUMNA DEL DATAFRAME")
print(df.max())

#-----------------------------------VALOR MAS BAJO DE UNA COLUMNA DEL DATAFRAME----------------------------------
print("VALOR MAS BAJO DE UNA COLUMNA DEL DATAFRAME")
print(df.min())

#-----------------------------------SELECCIONAR LA PRIMERA COLUMNA DEL DATAFRAME----------------------------------
print("SELECCIONAR LA PRIMERA COLUMNA DEL DATAFRAME")
print(df[0])

#-----------------------------------SELECCIONAR DOS COLUMNAS DEL DATAFRAME----------------------------------
print("SELECCIONAR DOS COLUMNAS DEL DATAFRAME")
print(df[[0,1]])

#-----------------------------------SELECCIONAR VALOR DE LA PRIMERA FILA Y ÚLTIMA COLUMNA DEL DATAFRAME----------------------------------
print("SELECCIONAR VALOR DE LA PRIMERA FILA Y ÚLTIMA COLUMNA DEL DATAFRAME")
print(df.iloc[0][2])

#-----------------------------------SELECCIONAR VALORES DE LA PRIMERA FILA DEL DATAFRAME----------------------------------
print("SELECCIONAR VALORES DE LA PRIMERA FILA DEL DATAFRAME")
print(df.loc[0])

#-----------------------------------SERIES----------------------------------
series = pd.Series({"Argentina":"Buenos Aires",
                    "Chile":"santiago de Chile",
                    "Colombia":"Bogotá",
                    "Perú":"Lima"
        })
print("SERIES")
print(series)