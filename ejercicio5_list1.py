# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:46:44 2022

@author: sebas

ingresar los valores de k y n para determinar cuantos autos pasan y cuantos 
quedan en taco.
"""
k, n = [int(i) for i in input().split()]
an = [int(i) for i in input().split()]
"""
con respecto a la cantidad de autos se genera una funcion suma
que permite contar los autos respecto a los minutos

"""
pasan = k*n 
if len(an) == n :
    def sumar(an):
        suma = 0 
        for numero in an:
            suma += numero
        return suma 
    if k*n < sumar(an):
       taco = (pasan - sumar(an))*(-1)
       print(taco)
    else:
        print(0)
else:
   print("no calza numero de intevalos de semaforos")

   