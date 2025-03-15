'''
Created on 14 mar. 2025

@author: eliumontoya


Un sistema de inicio de sesión que dé la bienvenida al cliente y, posteriormente, solicite su nombre de usuario y contraseña. El cliente tendrá un máximo de cuatro intentos para colocar correctamente su información; en caso de no lograrlo, la página se cerrará.
Al ingresar exitosamente en la página web, se mostrará un catálogo desplegado en forma matricial con, por lo menos, cuatro tipos de categorías de venta (por ejemplo, ropa para dama, caballero, niña y niño).
'''


Producto = (("Caballeros", "pantalon", "camisa","calcetin","corbata"),
            ("Damas", "falda", "blusa","blazer","tacones"),
            ("Niños", "mameluco", "playera","calcetin","jeans"),
            ("Niñas", "falda", "pijamas","moños","vestidos")
    )

def imprimirProducto():
    t = ""
    t = t + "".join("\n" + prod[0]+ ": " + "".join(p + " , " for p in prod[1:-1]) for prod in Producto)
    '''
     for prod in Producto:
        t = t + "\n" + prod[0]+ "  " + "".join(p + "," for p in prod[1:-1]) 
    '''
    t = t.replace(" , \n", "\n")
    print(t)

MAXIMO = 4
USER = "test"
PASS = "pass"

isValido = False
intentos = 0
while intentos < MAXIMO:
    usuario = input("Ingrese el usuario: ")
    passwd = input("Ingrese el pass: ")
    if usuario == USER and passwd == PASS:        
        isValido = True
        break
    intentos += 1
    print(f"Usuario o Contraseña incorrecta. Tiene {MAXIMO - intentos} intentos".title())

if isValido:
    imprimirProducto()
    
print("\nFin del programa".upper())