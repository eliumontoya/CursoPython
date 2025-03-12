'''
Created on 10 feb. 2025

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

Prueba tu código con los datos que hemos proporcionado.


Datos de Prueba
Entrada de muestra:

6
Salida esperada:

La altura de la pirámide es: 3
Output
Entrada de muestra:

20
Salida esperada:

La altura de la pirámide: 5
Output
Entrada de muestra:

1000
Salida esperada:

La altura de la pirámide: 44
Output
Entrada de muestra:

2
Salida esperada:

La altura de la pirámide: 1
'''

blocks = int(input("Ingresa el número de bloques: "))

sum = 0
height = 0
for i in range (1, blocks+1):
    sum += i
    if(blocks - sum > 0):
        height += 1


print("La altura de la pirámide:", height)


