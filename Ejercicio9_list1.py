# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:12:53 2022

@author: sebas
"""

n = int(input())
concursantes = []
for recorrido in range(n):
    equipo = input()
    concursantes.append(equipo) 
frecuencia = {}

"""
Al ingresar los n cantidad de equipos, Se genera un diccionario con el 
objetivo de asignarle a cada nombre(key) el conteo de la frecuencia
de dicho nombre para catalogar como spam 

Esto retorna de cualquier string si es que esta repetido dentro de la 
orden al ususario de nombre de equipo
"""


for n in concursantes:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1
            

for llave, valor in frecuencia.items():
    if (valor != 1) :
        print(llave)
        
    