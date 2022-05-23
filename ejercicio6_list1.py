# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:46:44 2022

@author: sebas
"""

n = int(input())
an = [int(i) for i in input().split()]
i = 0
hechizo = 0 
"""
El ciclo while permite al algoritmo ir de 3 numeros consecutivos 
hasta agotar la cantidad maxima de rango de lectura de lista "n-2"

se guarda la posicion de al medio una vez que se cumple que la suma
de los 3 elemetnos consecutivos sea la mas alta , almacenandolo
en un objeto "seccion" con la posicion de al medio i +2

se recorre con i+=1 para ir de iteracion  en iteracion.

"""
while i <  n-2 :
    sumatoria = an[i] + an[i + 1] + an[i+2]
    if sumatoria > hechizo:
        hechizo = sumatoria
        seccion = i + 2 
    i += 1 
print(hechizo,seccion)    
    
   




# for elemento in an:
#   if len(an) == n :
#       taco = (k - elemento)
#       print(taco)   