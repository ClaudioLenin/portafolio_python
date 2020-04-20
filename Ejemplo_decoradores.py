# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:32:09 2020

@author: claud
"""

def funcion_decoradora(funcion_parametro): #Recive un parametro que debe ser una funcion
    """Hola mundo"""    
    def funcion_interior(*args,**kwargs): #*parametros **clave valor argumento
        
        #Acciones adicionales que decoran
        
        print("Vamos a realizar un calculo: ")
        
        funcion_parametro(*args,**kwargs)
        
        #Acciones adicionales que decoran
        
        print("Hemos terminado el calculo")

    return funcion_interior

@funcion_decoradora
def suma(n1,n2,n3):
    print(n1+n2+n3)

@funcion_decoradora    
def resta(n1,n2):
    print(n1-n2)

@funcion_decoradora        
def potencia(base,exponente):
    print(pow(base,exponente))
    


suma(7,9,8)
resta(10,2)
potencia(base=5,exponente=3)

print(funcion_decoradora.__doc__)
help(funcion_decoradora)