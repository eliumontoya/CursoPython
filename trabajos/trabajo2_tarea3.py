'''
Created on 6 mar. 2025

@author: eliumontoya
'''
LIMITE = 21

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



