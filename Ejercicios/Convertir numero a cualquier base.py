+# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 00:46:06 2020

@author: claud
"""

def main():
    cantidad = int(input("Ingrese cantidad de números a evaluar: ")) #Ingreso de cantidad de números a evaluar
    i = 1 #Definir e iniciar contador de cantidad de números
    while i<=cantidad: #Definir condicion de parada del ciclo while
        numero = int(input("Ingrese el {}º número: ".format(str(i)))) #Ingresar el número a evaluar
        opcion = 0 #Definir e iniciar la opción de proceso para el ciclo while
        while opcion<1 or opcion>4: #Definir condicion de parada del ciclo while
            print("SELECCIONAR OPCIÓN") #Definir menú de opciones
            print()
            print("1. Binario") #Convierte el número ingresado en base binaria
            print("2. Octal") #Convierte el número ingresado en base octal
            print("3. Decimal") #Convierte el número ingresado en base decimal
            print("4. Hexadecimal") #Convierte el número ingresado en base hexadecimal
            opcion = int(input("opción:")) #Definir e ingresar la opción a evaluar
            cadena = "" #Definir la cadena que contendrá el nuevo número en cualquier base
            if opcion == 1: #Definir primera condición
                divisor = 2
            elif opcion == 2: #Definir segunda condición
                divisor = 8
            elif opcion == 3: #Definir tercera condición
                divisor = 10
            elif opcion == 4: #Definir cuarta condición
                divisor = 16
                
            while numero != 0: #Definir condición de parada de ciclo while
                    numero = numero / divisor #Quito el último digito del número ingresado
                    digito = numero // 1 % divisor #Obtengo el ultimo digito del numero
                    cadena = cadena + str(int(digito)) #Concatenar los digitos obtenidos
                    numero = int(numero) #Transformar el número obtenido en entero
            print(cadena) #Imprimir la cadena de digitos obtenida en cualquier base
        i = i + 1 #Incrementar condicion de parada del ciclo while
main()