import random
'''
Created on 24 nov. 2023

@author: eliumontoya
'''
 
#===============================================================================
# BUCLES
#===============================================================================

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)



#===============================================================================
# FOR CON UN WHILE CON CONTADOR
#===============================================================================
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)


#===============================================================================
# ## VALOR ALEATORIO
#===============================================================================
numero_aleatorio = random.randint(1, 10)
numero = int(input("ingresa un numero del 1 al 10, con 0 sales"))
while(numero != numero_aleatorio and numero != 0):
    print ("Estas atrapado en el loop infinito")
    numero = int(input("ingresa un numero del 1 al 10, con 0 sales"))
print("Has salido del loop, porque adivinaste el numero el cual era", numero_aleatorio)


#===============================================================================
# DULCES SINTACTICOS: BREAK Y CONTINUE
#===============================================================================

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")



#===============================================================================
# FOR CON ELSE
#===============================================================================

for i in range(5):
    print(i)
else:
    print("else:", i)


n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")





#===============================================================================
# Lothar Collatz 
#===============================================================================

'''
toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
si es par, evalúa un nuevo c0 como c0 ÷ 2;
de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
si c0 ≠ 1, salta al punto 2.
'''
c0  = int(input("Ingresa c0 mayor a 0"))
while c0 > 1:
    print ("co: ", c0)
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3 * c0 + 1
    
print ("Salió con co",c0)