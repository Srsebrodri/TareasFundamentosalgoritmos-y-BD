# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:55:37 2022

@author: sebas
"""
#ejercicio1
"""
Acontinuacion se pide al usuario ingresar los valores de la cantidad de paneles "N" 
y sus respectivas dimensiones en la posicion 1 y 2 de la lista.

"""

N = input()
ThS2 = N.split() 
"""
En base a las posiciones respectivas se calcula la cantidad de sulfuro de torio en nanogramos
requeridas sacando areas ( posicion 1 * posicion 2 de lista THS2) multiplcando por la cantidad
de paneles y *2 debido a ambas caras del panel.

se imprime cantidad de nanogramos.

"""
ng_ThS2 = int(ThS2[0]) * int(ThS2[1]) * int(ThS2[2]) * 2
print(ng_ThS2)
