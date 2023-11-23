'''
Created on 22 nov. 2023

@author: eliumontoya
'''

## Abreviaciones
var= 0
i= 0 
j= 0 
rem= 0 
x = 0

i = i + 2 * j
i += 2 * j

var = var / 2
var /= 2
rem = rem % 10
rem %= 10
j = j - (i + var + rem)
j -= (i + var + rem)
x = x ** 2
x **= 2


## Operadores cadena
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


## Conversiones de tipos
x = int("0")
y = float("0.4")
z = str(0.4)

## Saber el tipo de clase
print (type(x))
print (type(y))
print (type(z))
 