'''
Created on 22 nov. 2023

@author: eliumontoya
'''
print(True > False)
print(True < False)



## Redondeo hacia abajo
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

## Prioridades de potencia es al reves: de derecha a izq.
print(2 ** 2 ** 3)



## Ejercicios de prioridades

print((2 ** 4), (2 * 4.), (2 * 4))



print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))



print((2 ** 4), (2 * 4.), (2 * 4))

#===============================================================================
# Deplazamiento de bits
#===============================================================================
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
'''
17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)
'''


