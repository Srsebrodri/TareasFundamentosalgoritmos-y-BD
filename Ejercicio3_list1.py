# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:55:37 2022

@author: sebas
"""

# ejercicio3 
"""
ingresar los valores de a y b que corresponden a las claves actuales de los 
candados 1 y 2 respectivamente 
"""
a = int(input())
b = int(input())

"""
se genera la condicion de que si cumple aunque sea una de las siguientes condiciones:
    uso de operador logico "or" 
    1er candado tiene clave un numero par 
    2do candado tiene clave impar 
el ladron daria con la clave tarde o temprano si empezo desde el  "0000" 
e.o.c
nunca dara con la clave 
"""
if a%2 == 0 or b%2 == 1 :
    print("yes")
else:
  print("no")

#ejercicio 4

