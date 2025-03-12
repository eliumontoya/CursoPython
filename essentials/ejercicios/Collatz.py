'''
Created on 10 feb. 2025

@author: eliumontoya
En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
si es par, evalúa un nuevo c0 como c0 ÷ 2;
de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
si c0 ≠ 1, salta al punto 2.

'''
from pickle import FALSE

def validaImpar(c0):
    if c0 % 3 == 0:
        return True
    return False


def validaPar(c0):
    if c0 % 2 == 0:
        return True
    return False
    
def ejecutaPar(c0):
    c0 = c0 / 2
    print ("p", str(c0))
    return c0

def ejecutaImpar(c0):
    c0 = 3 * c0 + 1
    print ("i", str(c0))
    return c0

c0 = int(input("numero"))

while c0 > 1:
    if validaPar(c0):
        c0 = ejecutaPar(c0)
    elif validaImpar(c0):
        c0 = ejecutaImpar(c0)
        continue
    
print ("Final ". c0)