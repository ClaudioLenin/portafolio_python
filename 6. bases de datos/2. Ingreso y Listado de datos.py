# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:08:55 2020

@author: claud
"""

import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #Crear una tabla forma 1

#miCursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMEMENT,NOMBRE_ARTICULO VARCHAR(50) UNIQUE, PRECIO INTEGER, SECCION VARCHAR(20))") #Crear una tabla forma 2

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')") #Forma 1 de ingresar un registro

variosProductos = [
            ("Camiseta",10,"Deportes"),
            ("Jarrón",90,"Cerámica"),
            ("Camión",20,"Juguetería"),
            ("Pantalón",20,"Jersy")
        ]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos) #Forma 2 de ingresar varios registros

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(,?,?,?)",variosProductos) #Forma 3 de ingresar varios registros

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

#print(variosProductos)
for producto in variosProductos:
    print(producto[0])

miConexion.commit()

miConexion.close()
