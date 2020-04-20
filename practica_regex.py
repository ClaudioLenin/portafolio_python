# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:33:32 2020

@author: claud
"""
import re

cadena = "Vamos a aprender expresiones regulares"

textoBuscar = "aprender"

textoEncontrado = re.search(textoBuscar,cadena)

print(textoEncontrado.start()) #Caracter de inicio

print(textoEncontrado.end()) #Caracter fin

print(textoEncontrado.span()) #Caracter de inicio y fin

print(re.findall(textoBuscar,cadena))
print(len(re.findall(textoBuscar,cadena)))

"""if re.search(textoBuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")"""

#-----------------------------------------ANCLAS---------------------------------------------------

lista_nombres = [
        'Pepito Seresoyo',
        'Tobias Oso',
        'Saltin Salty',
        'Boton Boto',
        'Tobias Peluche',
        'niños',
        'niñas',
        'camion',
        'camión'
        ]
for elemento in lista_nombres:
    #if re.findall('^Tobias',elemento): #Busqueda comienza con:
    #if re.findall('Oso$',elemento): #Busqueda termina con:
    """if re.findall('[O]',elemento): #Busqueda de un caracter en específico
        print(elemento)"""
    """if re.findall('niñ[oa]s',elemento): #Busqueda de un caracter en específico
        print(elemento)"""
    """if re.findall('cami[oó]n',elemento): #Busqueda de un caracter en específico
        print(elemento)"""
    if re.findall('[a-m]',elemento): #Busqueda de un caracter en específico
        print(elemento)

#-----------------------------------------MATCH---------------------------------------------------
nombre1 = "Jara López"    
nombre2 = "Antonio Gómez"
nombre3 = "Lara López"    

#if re.match("Sandra",nombre3,re.IGNORECASE):
#if re.match("\d",cadena2): #Para buscar numeros
#if re.search("Claudio",nombre3): #Buscar cadenas de texto
if re.match(".ara",nombre3,re.IGNORECASE):
    print("Sila")
else:
    print("Nola")