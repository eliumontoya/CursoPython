'''
Created on 30 nov. 2023

@author: eliumontoya
'''

#===============================================================================
# Listas que son Mutables con  []
#===============================================================================


numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.


#===============================================================================
# Lista anidada
#===============================================================================
my_list = [1, 'a', ["lista", 64, [0, 1], False]]

print (my_list)


#===============================================================================
# Borrar listas y elementos
#===============================================================================
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # output: [1, 2, 4]

del my_list  # borra la lista entera



#===============================================================================
# Longitud de lista
#===============================================================================
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(my_list))  # output 5
 
del my_list[2]
print(len(my_list))  # output 4

