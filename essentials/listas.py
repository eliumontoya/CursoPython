


'''
Created on 30 nov. 2023

@author: eliumontoya
'''







def RevisarSiExiste( ):
    my_list = [0, 3, 12, 8, 2]
    print(5 in my_list)
    print(5 not in my_list)
    print(12 in my_list)

def Rebanar( ):
    my_list = [10, 8, 6, 4, 2]
    new_list = my_list[1:3]
    print(new_list)
 
def Ordenar():
    lst = [5, 3, 1, 2, 4]
    print(lst)
    lst.sort()
    print(lst) # output: [1, 2, 3, 4, 5]
    lst.reverse()
    print(lst) # output: [5, 4, 3, 2, 1]

def IntercambioValores( ):
    variable_1 = 1
    variable_2 = 2
    variable_1, variable_2 = variable_2, variable_1
    my_list = [10, 1, 8, 3, 5]
    my_list[0], my_list[4] = my_list[4], my_list[0]
    my_list[1], my_list[3] = my_list[3], my_list[1]
    print(my_list)
 
def Anexar( ):
    numbers = [111, 7, 2, 1]
    numbers.append(4)
    print(len(numbers))
    print(numbers)
###
    numbers.insert(0, 222)
    print(len(numbers))
    print(numbers)

def IndicesNegativos( ):
    numbers = [111, 7, 2, 1]
    print(numbers[-1]) ## Imprime 1
    print(numbers[-2]) ## Imprime 2
 
def Longitud( ):
    my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
    print(len(my_list)) # output 5
    del my_list[2]
    print(len(my_list)) # output 4
 
def Borrar():
    my_list = [1, 2, 3, 4]
    del my_list[2]
    print(my_list) # output: [1, 2, 4]
    del my_list # borra la lista entera

def Anidadas():
    my_list = [1, 'a', ["lista", 64, [0, 1], False]]
    print(my_list)
 
def Listas():
    numbers = [10, 5, 7, 2, 1]
    print("Contenido de la lista original:", numbers) # Imprimiendo el contenido de la lista original.
    numbers[0] = 111
    print("\nContenido de la lista con cambio:", numbers) # Imprimiendo contenido de la lista con 111.
    numbers[1] = numbers[4] # Copiando el valor del quinto elemento al segundo elemento.
    print("Contenido de la lista con intercambio:", numbers) # Imprimiendo contenido de la lista con intercambio.
    print("\nLongitud de la lista:", len(numbers)) # Imprimiendo la longitud de la lista.
 
def Clonar():
    l = [0, 3, 4, 3]
    a = l
    del l[0]
    l.append("object")
    print(a)
    print(l)


 
#===============================================================================
# Listas que son Mutables con  []
#===============================================================================
print ("== Ejercicio:  Listas que son Mutables con  [] ==")

Listas()


#===============================================================================
# Lista anidada
#===============================================================================
print ("== Ejercicio:  Lista anidada ==")

Anidadas()


#===============================================================================
# Borrar listas y elementos
#===============================================================================
print ("== Ejercicio:  Borrar listas y elementos ==")

Borrar()



#===============================================================================
# Longitud de lista
#===============================================================================
print ("== Ejercicio:  Longitud de lista ==")
Longitud( )


#===============================================================================
# Indices Negativos
#===============================================================================
print ("== Ejercicio:  Indices Negativos ==")
IndicesNegativos( )



#===============================================================================
# Anexar valores a listas
#===============================================================================
print ("== Ejercicio:  Anexar valores a listas ==")

Anexar( )


#===============================================================================
# Intercambio de valores
#===============================================================================
print ("== Ejercicio:  Intercambio de valores ==")
IntercambioValores( )


#===============================================================================
# Ordenar listas
#===============================================================================
print ("== Ejercicio:  Ordenar listas ==")

Ordenar()


#===============================================================================
# Clonar listas
#===============================================================================

print ("== Ejercicio:  Clonar listas ==")

Clonar()




#===============================================================================
# Rebanada de lista
#===============================================================================
print ("== Ejercicio:  Rebanada de lista ==")

Rebanar( )

#===============================================================================
# Revisar si existe en lista
#===============================================================================
print ("== Ejercicio:   Revisar si existe en lista ==")
RevisarSiExiste( )
