# -*- coding: utf-8 -*-
""" 
este ejercicio fue realizado por  Vladislav Ershov en 2019
"""

n = int(input())
fila = []
for i in range(n):
    numeros = input().split()
    fila.append(numeros)
""" 
Dentro de las solicitud al usuario se pide la cantidad de filas "n"
para generar la matriz y ver el recorrido especifico que se debe ejecutar
para dar el orden ascendiente de los valores en muestra.

toda operacion se guardara dentro de un objeto de tipo string "string"
"""    
string = ''

""" 
La matriz inicia con el primero valor de la primera lista 1
recorre un numero hacia abajo "i" y luego desde el anterior posicion (pivote)
se avanza hacia la derecha "j"
"""

for i in range(n):
        j = 0
        while i >= 0:
                string += (fila[i][j] + ' ')
                i -= 1
                j += 1

""" 
Esto se hace sucesivamente hasta que ya no puedes seguir recorriendo elementos
de la lista en la cual esta la matriz.
Para esto es que se inicia otro ciclo for para avanzar hasta encontrar 
con una lectura de tope rango n.

inicializando la k en n-1 permite dar con la posicion que sigue
diagonalmente la lectura de la matriz, generando la sucesion completa 
solicitada
"""                
for i in range(1,n):
        k = n - 1
        while i != n:
                string += (fila[k][i] + ' ')
                k -= 1
                i += 1
print(string)

