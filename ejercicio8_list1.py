# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input())
nombre = []
for recorrido in range(n):
    invitados = input()
    nombre.append(invitados) 
    
"""
Una vez creada la lista de invitados , se le asignan diferentes ciclos 
for bajo la condicion de que si dentro del string encuentra el 
string "+" , detiene la busqueda y genera una lista con el valor 2 o 1 
respectivamente si es que viene con acompañante.

para dar como resultado final el valor total multiplicando por el valor
por cabeza de $100 y sumandole los $200 de andres y maria
"""    
valores = []
resultado = 0          
for i in nombre:
   
   for j in i:
       if (j == '+') :
           resultado = 2 
           break
           
       else:
           resultado = 1 
   valores.append(resultado)           
       
def sumar(valores):
    if valores == []:
        return 0
    else:
        return valores[0] + sumar(valores[1:])

cuenta = sumar(valores)*100 + 200
print(cuenta)
                    
       

        
    


    