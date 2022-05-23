# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:22:04 2022

@author: sebas
"""

n1 = int(input())
alfa =set([int(i) for i in input().split()])
n2 = int(input())
beta = set([int(i) for i in input().split()])
n3 = int(input())
gama = set([int(i) for i in input().split()])

"""
Al ingresar los valores de las diferentes entradas de datos, se transforma el
input a un set de conjuntos , permitiendo las intersecciones de conjuntos
de manera eficiente
"""

interseccion = alfa.intersection(beta) and alfa.intersection(gama)
print(len(interseccion))