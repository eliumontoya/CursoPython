'''
Created on 6 mar. 2025

@author: eliumontoya
0|    1    2    3    4    5    6    7    8    9    10    

-    -    -    -    -    -    -    -    -    -    -    

1|    1    2    3    4    5    6    7    8    9    10
2|    2    4    6    8    10    12    14    16    18    20
3|    3    6    9    12    15    18    21    24    27    30
4|    4    8    12    16    20    24    28    32    36    40
5|    5    10    15    20    25    30    35    40    45    50
6|    6    12    18    24    30    36    42    48    54    60
7|    7    14    21    28    35    42    49    56    63    70
8|    8    16    24    32    40    48    56    64    72    80
9|    9    18    27    36    45    54    63    72    81    90
10|    10    20    30    40    50    60    70    80    90    100

Elabora un programa que muestre en pantalla una tabla de Pitágoras como la siguiente:


Posteriormente, debes solicitar dos factores al usuario para realizar la multiplicación.
Por último, debes mostrar en pantalla el resultado de la multiplicación.
Estas son las restricciones para realizar el programa:

La tabla de Pitágoras debe estar almacenada en una lista de listas (matriz).
La tabla debe mostrarse con una función que no regresa valor y, además, aparecer sin los corchetes ni comas que evidencian la impresión común de una matriz.
La multiplicación se realizará mediante una función que regresa un valor, usando la lista de listas; por tanto, no se permite el uso del operador correspondiente (*).
Tienes total libertad para crear la lista de listas, ya sea de forma directa, con un ciclo for o con una expresión generadora.
El programa debe mostrar la tabla de Pitágoras, así como el resultado de la multiplicación de los valores proporcionados por el usuario.


'''
LIMITE = 11

def lista(step):
    return list (range(1*step,LIMITE*step, step))

def printHeaderRow(): 
    print ("".join("-"  + "\t" for y in range(LIMITE) )+"\n")
    
    
def printHeaders():
    t = "0|\t" +"".join( str(y)  + "\t" for y in range(1,LIMITE) ) 
    print (t+"\n")
    printHeaderRow() 
        

def imprimirCol(i, x):
    t = str(i) + "|" +"".join("\t" + str(columna) for columna in x)
    return t

def imprimir(m):
    printHeaders()
    i = 1
    for renglon in m:                
        print ( imprimirCol(i, renglon) )
        i += 1

m = []
for i in range (1,LIMITE):
    m.append(lista(i))

imprimir(m)





def listaRec(n,step):
    if step < LIMITE-1:
        n[step] = listaRec(n,step+1)        
    return list (range(1*step,LIMITE*step, step) )

def hacerValidaciones(x,y):
    if x >= LIMITE or y >= LIMITE:
        raise Exception()
    if x < 0  or y < 0 :
        raise Exception()
            

def pedirNumeros():
    print(f"Dame un valor del 1 al {LIMITE-1}")
    x = int(input())
    print(f"Dame otro valor del 1 al {LIMITE-1}")
    y = int(input())
    return x, y

def solicitarValores():
    x = y = 0
    while True:
        try:
            x, y = pedirNumeros()
            hacerValidaciones(x,y)
        except:
            print(f"Deben ser numericos del 1 al {LIMITE - 1}: Va otra vez ...")
        else:
            break
    
    return x,y

def obtenerResultado(n,x,y):
    return n[x-1][y-1]



print("\n\n")


n = list(range(LIMITE-1))
n[0] = listaRec(n, 1) 
imprimir(n)
x,y = solicitarValores()
print (f"El resultado es {obtenerResultado(n,x,y)}")



