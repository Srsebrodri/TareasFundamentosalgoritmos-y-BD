# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:28:26 2022

@author: sebas

Se inicia solicitando al usuario ingresar la cantidad de trozos N y la 
capacidad K para cocinar en base a la orden que llega a la cocina
"""
N,K = [int(i) for i in input().split()]
"""
Se condiciona que la capacidad k sea mayor a 0 para poder imprimir
un resultado.

Sucesivamente se le brindan distintos escenarios para imprimir el tiempo 
total de coccion de N trozos de salmones

escenario1: Si las cantidades de salmones son menores a la capacidad
imprimir 2 minutos

escenario2: si las cantidades de salmones son el doble a la capacidad el
el tiempo resultaria al doble de la capacidad K

escenario3: si el valor de N es mayor a K y menor al doble de K
el tiempo se condiciona a que si dependiendo del resto del cuociente
entre los trozos N y capacidad K.
  si: es menor a 0.5 , le añade 1 minuto extra al tiempo de coccion 
      con respecto al doble de la capacidad.
    e.o.c 
      le añade 2 minutos con respecto al doble de la capacidad 
      
"""
if K>0 : 
    
  if (N <= K):
    print(2)
    
  elif (N%K == 0):
    print((N/K)*2)
  else:
      if (N > K) and (N < 2 * K):
        if (N-K > K/2):
         print((2+(N//K*2)))
        else:
         print((1+(N//K*2)))
    
    


  