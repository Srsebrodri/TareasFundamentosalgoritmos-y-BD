# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:55:37 2022

@author: sebas
"""

# ejecicio 2
"""
se ingresa el numero de mounstros N
"""
N = int(input()) 

"""
En base al rango en que se clasifica el numero N , se imprime el valor
categorizado .

de 1 a 4
few
de 5 a 9
several
de 10 a 19
pack
de 20 a 49
lots
de 50 a 99
horde
de 100 a 249
throng
de 250 a 499
swarm
de 500 a 999
zounds
a partir de 1000
legion

de 5 a 9-->several

de 10 a 19-->pack

de 20 a 49-->lots

de 50 a 99-->horde

de 100 a 249-->throng

de 250 a 499 -->swarm

de 500 a 999 --> zounds

a partir de 1000 --> legion
"""
if N >= 1 and N <= 4 :
    print('few')
elif N >= 5 and N <= 9:
    print('several')
elif N >= 10 and N <= 19:
    print('pack')  
elif N >= 20 and N <= 49:
    print('lots')    
elif N >= 50 and N <= 99:
    print('horde') 
elif N >= 100 and N <= 249:
    print('throng')
elif N >= 250 and N <= 499:
    print('swarm') 
elif N >= 500 and N <= 999:
    print('zounds') 
else :
    print('legion')      


      
        
      