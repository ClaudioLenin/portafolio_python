# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:12:53 2020

@author: claud
"""

def main():
    
    cantidad = int(input('Ingrese cantidad de números: '))
    i = 1
    
    while i <= int(cantidad):
        numero = int(input('Ingrese {}º número: '.format(str(i))))
        numero = int(numero)
        numero_digitos = cantidad_digitos(int(numero))
        sumador_posiciones_pares = 0
        bandera = True #Condición de salida de if
        while numero != 0: #Condicion de parada del ciclo while
            digito = int(numero) // 1 % 10 #Obtengo el ultimo digito del numero
            digito = int(digito) #Transformo el digito obtenido en entero
            numero = int(numero) / 10 #Quito el último digito del número ingresado
            numero = int(numero) #Transformo el número obtenido en entero
            
            if bandera: #Primera asignacion de digito menor
                digito_menor = digito #Determino valor por defecto del valor minimo
                bandera = False #Cambio estado para ya no entrar en esta condicion
            elif  digito <= digito_menor: #Comparo si mi digito actual es menor que el digito anterior
                digito_menor = digito #Asigno nuevo valor a digito menor
                
            if digito // 1 % 2 == 0: #verifico si el digito actual es par
                sumador_posiciones_pares = sumador_posiciones_pares + numero_digitos #Incremento la cantidad de sumador de posiciones pares
            
            numero_digitos = numero_digitos - 1 #Resto la cantidad de digitos del numero
            
        print('El digito menor es: {} y la suma de las posiciones de los elementos pares es: {} '.format(str(digito_menor),str(sumador_posiciones_pares)))
        i = i+1 #Incremento condicion de parada del while
        
def cantidad_digitos(num):
    cantidad = 0 #Establecer valor por defecto del contador de digitos
    while int(num) != 0: #Condicion de parada del ciclo while
        num = int(num) / 10 #Quito el último digito del número ingresado
        cantidad = cantidad + 1 #Incremento cantidad de digitos que tiene el número
    return cantidad #Devolver la cantidad de digitos del número
    
        
main()


        
        