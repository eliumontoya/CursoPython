'''
Created on 9 feb. 2025

@author: eliumontoya
'''

def fibonacci(i, max):
    if i == max:
        return i
    return  i + fibonacci(i+1,max)

def fib(max):
    print (fibonacci(0,max))

fib(50)

'''
1
2 3
3 6
4 10
5 15
6 21
7 28
8 36
9 45
10 55 
'''
