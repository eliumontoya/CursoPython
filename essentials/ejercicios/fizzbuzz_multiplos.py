'''
Created on 9 feb. 2025

@author: eliumontoya
'''

def multiploDe3(i):
    if i % 3 == 0:
        return "fizz"
    return ""

def multiploDe5(i):
    if i % 5 == 0:
        return "buzz"
    return ""

def extra(i):
    return str(multiploDe3(i)) + str(multiploDe5(i))
    
for i in range (101):
    print (i,extra(i))
