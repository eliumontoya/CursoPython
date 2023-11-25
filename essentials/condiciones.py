'''
Created on 23 nov. 2023

@author: eliumontoya
'''
from numpy.core.defchararray import upper, lower
 
ns = [55,99,100,101,-5,123]
for n in ns:
    print (n >= 100 )
    
    
## if else elif
if n > 100:
    print (100)
elif n> 50:
    print (50)
elif n >= 0:
    print ("posivito")
else:
    print ("negativo")
    
## if else de una instruccion solo en una linea
x = 0
y = 0
larger_number = 0

if x > y: larger_number = x
else: larger_number = y

## Numero mas grande con MAX y MIN
x = 2345
y = 346
z = 234
print ( "Max: ",max(x, y, z))
print ( "Min: ",min(x, y, z))

##
letra = "ESPATIFILIO"
le = input("ingresa texto ESPATIFILIO si gustas")
if le == upper(letra): print ("ESPATIFILIO")
elif le == lower(letra): print ("No, ¡quiero un gran Espatifilo!")
else: print ("¡Espatifilo!, ¡No", le + "!")