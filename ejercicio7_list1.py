# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n1 = int(input())
alfa = [int(i) for i in input().split()]
n2 = int(input())
beta = [int(i) for i in input().split()]
n3 = int(input())
gama = [int(i) for i in input().split()]

lista = alfa + beta + gama 

frecuencia = {}

for n in lista:
    if n in frecuencia:
        frecuencia[n] += 1 
    else:
        frecuencia[n] = 1 

Conteo = list(frecuencia.values())
print(Conteo.count(3))
    
#preguntar por la logica de si necesita contar los numeros repetidos en una fila de n indice i

