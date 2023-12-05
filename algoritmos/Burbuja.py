'''
Created on 5 dic. 2023

@author: eliumontoya
'''
isAscendente = False
lista = [34,123,6,2,3,7,78,21,34,456,0,-1,245]
for i in range(len(lista)):
    for j in range(len(lista) - 1):
        intercambio = False
        if isAscendente: ## de menor a mayor
            if (lista[j] > lista[j+1]): #si es mayor al siguiente cambiamos
                intercambio = True
        else: #de mayor a menor
            if(lista[j] < lista[j+1]): #si es menor al siguiente cambiamos
                intercambio = True
                
        if intercambio:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            continue
print(lista)