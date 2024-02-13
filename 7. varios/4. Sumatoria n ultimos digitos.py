# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:50:59 2020

@author: claud
"""
def main():
    cantidad = int(input('Ingrese cantidad de números:'))
    i = 1
    while i <= cantidad:
        numero = int(input('Ingrese {}º número:'.format(str(i))))
        contador = 0
        auxiliar = numero
        while int(auxiliar) != 0:
            auxiliar/=10
            contador+=1
        num_digito = 0
        while num_digito <=0 or num_digito > contador:
            num_digito = int(input('Ingrese posición de digito:'))
        contador_digitos = 0
        digitos = 0
        while int(numero) != 0:
            if contador_digitos >= num_digito:
                digitos += numero//1%10
            numero /= 10
            contador_digitos += 1
        print('El número tiene {} digitos y la suma de los n digitos es {}'.format(str(contador),str(digitos)))
        
        
main()