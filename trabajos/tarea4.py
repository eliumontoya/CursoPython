import random
'''
Created on 11 mar. 2025

@author: eliumontoya
Parte 1. Realiza lo siguiente:

Convierte cada categoría del catálogo en un diccionario y, a cada una de ellas, agrega tres piezas a la venta, por lo menos.
Crea dos tuplas para cada pieza: una para talla (CH, M, G y XG) y una para color (negro, blanco, azul y rosa).
Solicítale al usuario que genere un documento con la clave (key) de la ropa elegida, pero agregando la talla seleccionada. Por ejemplo:
Key

Producto

PMH

Pantalón de mezclilla para hombre


Si el usuario elige la talla G, en un archivo debe anotarse PMH – G.

Crea, por lo menos, tres excepciones para algunos productos que no cuenten con las tallas chica o grande; en estos casos, se hará la devolución del dinero.
Solicita la lectura del documento creado por el usuario y agrega los precios unitarios a cada pieza; entonces, si una pieza se compra en talla XG, tendrá un 10% de descuento.
Finalmente, realiza la suma del costo total de los productos y añade un monto extra de envío, ya sea general o dependiendo de las piezas adquiridas. Imprime esta cuenta, en el monitor o en un archivo, para que el usuario la pueda revisar.
'''


'''
Vamos a crear un diccionario con el formato:
caballeros: { sku1001 : {articulo: playera, inventario: 10, precio: 30.2, tamano:[CH,M], color:[negro,azul]},
 sku1002 : {articulo: pantalon, inventario: 10, precio: 30.2, tamano:[CH,M], color:[negro,azul]},
  sku1003 : {articulo: camisa, inventario: 10, precio: 30.2, tamano:[CH,M], color:[negro,azul]}
}

'''

## TUPLAS CON LOS VALORES PERMITIDOS
CATEGORIAS = ("caballeros", "damas", "niños", "niñas")
COLORES = ("negro", "blanco", "azul", "rosa")
TALLAS = ("CH", "M", "G", "XG")
PRODUCTOS = ("playera","pantalon","camisa","calzon","calcetin","chamarra","sueter")

Articulos = {}
'''
----------- FUNCIONES PARA CREAR LOS PRODUCTOS, CATEGORIAS, ETC. 
'''

def adivinarTotalProductos():
    return random.choices(PRODUCTOS,k=random.randint(1, 7))

def crearTamanos():
    return random.choices(TALLAS,k=random.randint(1, 4))

def crearColores():
    return random.choices(COLORES,k=random.randint(1, 4))

def crearPrecio():
    return random.uniform(0.0,100.99)

def crearInventario():
    return random.randint(0,10)



'''
Funcion inicial que crea el diccionario de Articulos desde las categorias
'''
def crearCategorias():
    for categoria in CATEGORIAS:
        Articulos[categoria] = crearArticulos() ## Agregamos el diccionarios de muchos productos

def crearArticulos():
    prods = {}
    for producto in adivinarTotalProductos():
        sku = crearSKU(prods)
        articulo = crearArticulo(producto)
        prods[sku] = articulo
    return prods
    
def crearSKU(prodsExistentes):
    sku = ""
    while True:
        sku = "SKU" + str(random.randint(10000, 90000))
        if not sku in prodsExistentes:
            break
    return sku

'''
Regresa: {articulo: playera, inventario: 10, precio: 30.2, tamano:[CH,M], color:[negro,azul]},
'''
def crearArticulo(producto):
    art = {}
    art["articulo"] = producto
    art["inventario"] = crearInventario()
    art["precio"] =  crearPrecio()
    art["tamano"] =  crearTamanos()
    art["color"] =  crearColores()
    return art

'''
----------- FUNCIONES PARA IMPRIMIR LOS PRODUCTOS, CATEGORIAS, ETC. 
'''

def unpackList(list):
    return  "".join( str(i)+", " for i in list)
    
def mostrarCategoriasDisponibles():
    t = ""
    for categoria in Articulos.keys():
        t  += categoria + "\n"
    print (t)      
    
def imprimirArticulos(categoria): 
    t = ""
    for sku in Articulos[categoria].keys():
        t = t + "\t" + sku + "\n"
            
        t = t + "\t\t articulo: " + Articulos[categoria][sku]["articulo"] + "\n" 
        t = t + "\t\t inventario: " + str(Articulos[categoria][sku]["inventario"]) + "\n" 
        t = t + "\t\t precio: " + str(Articulos[categoria][sku]["precio"] ) + "\n" 
        t = t + "\t\t tamanos: " + unpackList( Articulos[categoria][sku]["tamano"] ) + "\n" 
        t = t + "\t\t colores: " + unpackList( Articulos[categoria][sku]["color"] ) + "\n" 
    return t        
            
def imprimirCategorias():
    t = ""
    for categoria in Articulos.keys():
        t  += categoria + "\n"
        t += imprimirArticulos(categoria)
        t += "\n"
    print (t)       
    
'''
----------- FUNCIONES PARA IMPRIMIR Y EJECUTAR EL MENU
'''
 
OPCIONES_MENU = {"SALIR": 0,
                 "TODO": 1,
                 "CATEGORIAS":2,
                 "PRODUCTOS": 3,
                "CHECKIN": 4,
                 "CARRITO": 5,
                 "CHECKOUT": 6
                 }


def mostrarMenu():   
    print (f'''
Bienvenido
Ingrese la opcion deseada:
{OPCIONES_MENU["TODO"]}) Mostrar todo el catalogo    
{OPCIONES_MENU["CATEGORIAS"]}) Mostrar solo las categorias disponibles
{OPCIONES_MENU["PRODUCTOS"]}) Mostrar los productos de la categoria deseada
{OPCIONES_MENU["CHECKIN"]}) Agregar un producto al carrito
{OPCIONES_MENU["CARRITO"]}) Revisar el carrito de compras
{OPCIONES_MENU["CHECKOUT"]}) Hacer Checkout
{OPCIONES_MENU["SALIR"]}) Finalizar
    
    ''')
    
def opcionValida(t):
    if t in list( OPCIONES_MENU.values() ):
        return True
 
    return False
    
    
def solicitarOpcion():
    t = int( input() )
    if not opcionValida(t):
        raise Exception()
    return t

    
def leerCategoria():
    while True:
        t = input()
        if t in Articulos:
            return t
    
def ejecutarOpcion(opcion):
    if opcion == OPCIONES_MENU["TODO"]:
        ejecutarOpcionTodo()
    elif opcion == OPCIONES_MENU["CATEGORIAS"]:
        ejecutarOpcionCategorias()
    elif opcion == OPCIONES_MENU["PRODUCTOS"]:
        ejecutarOpcionProductos()        
    elif opcion == OPCIONES_MENU["CHECKIN"]:
        ejecutarOpcionAgregarCarrito()     
    elif opcion == OPCIONES_MENU["CARRITO"]:
        ejecutarOpcionVerCarrito()     
    elif opcion == OPCIONES_MENU["CHECKOUT"]:
        ejecutarOpcionCheckoutCarrito()      
        
        
'''
----------- FUNCIONES PARA EJECUTAR CADA UNO DE LOS MENUS
'''
        

def ejecutarOpcionTodo():
    imprimirCategorias()
    
def ejecutarOpcionCategorias():
    mostrarCategoriasDisponibles()
    
def ejecutarOpcionProductos():
    print ("Estas son las categorias disponibles:\n")
    mostrarCategoriasDisponibles()
    print("\nEscriba la categoria de la que quiere ver los productos")
    categoria = leerCategoria()
    print("Articulos de: ", categoria)
    print (imprimirArticulos(categoria) )
    
Carrito = {}
def ejecutarOpcionAgregarCarrito():
    while True:
        print("\n\nIngrese un SKU valido o  presione enter (VACIO) para regresar al menu anterior")
        sku = input()
        if sku == "":
            return
        try:
            prod = validarSKUParaCheckin(sku)
            Carrito[sku] = prod
            print(f"Agregando {sku} al carrito exitosamente".title())
        except Exception as e:
            print(type(e),"Error: ", e)
            
def validarSKUParaCheckin(sku):
    ## Validamos que sea un SKU existente
    productoSKU = validarSKUExistente(sku)
    ## Validamos que haya del tamaño
    tamano = solicitarTamano(sku, productoSKU)
    ## Validamos que haya del color
    color = solicitarColor(sku, productoSKU)
    ## Validamos que haya inventario
    cantidad = solicitarCantidad(sku, productoSKU)
    return crearProductoParaCarrito(tamano= tamano, color= color, cantidad= cantidad, precioLista = productoSKU["precio"])
    
def crearProductoParaCarrito(tamano,color, cantidad, precioLista):
    t = {}
    t["cantidad"] = cantidad
    t["tamano"] = tamano
    t["color"] = color
    t["precioLista"] = precioLista
    return t

def ejecutarOpcionVerCarrito():
    print("El carrito contiene:")
    print(getCarrito())

def getCarrito():
    t = ""
    for producto in Carrito.keys():
        t = t + producto +" - cantidad: "+str(Carrito[producto]['cantidad']) + " - tamano: " + Carrito[producto]['tamano'] + " - color: " + Carrito[producto]['color']+"\n"
    return t
                 
def ejecutarOpcionCheckoutCarrito():
    file = open("carrito.txt","w")
    file.write(getCarrito())
    file.close()
    print("Guardando carrito en archivo")
    imprimirTotalCarrito()
    #Carrito.clear()

def calcularDescuento(producto):
    descuento = 0
    
    ## 10% si se lleva mas de 3
    if Carrito[producto]['cantidad'] > 3:
        descuento += Carrito[producto]['precioLista'] * .90 - Carrito[producto]['precioLista']
    ## 5% si se lleva XG
    if Carrito[producto]['tamano'] == "XG":
        descuento += Carrito[producto]['precioLista'] * .95 - Carrito[producto]['precioLista']
    ## 15% si se lleva blanco
    if Carrito[producto]['color'] == "blanco":
        descuento += Carrito[producto]['precioLista'] * .85 - Carrito[producto]['precioLista']
    return abs(descuento)
      
def calcularEnvio(subtotal,cantidadProd):
    
    envio = abs(subtotal * .95 - subtotal)
    if(cantidadProd > 15):
        envio *= 1.10
    return envio
  
def mostrarLeyendaDescuento():
    print('''
    Condiciones de Descuento:
    10% más de 3
    5% para XG
    15% para colores blancos
    ''')

def mostrarLeyendaEnvio():
    print('''
    Condiciones de Envio:
    5% más de envio
    10% extra para más de 15 productos
    ''')
    
def imprimirTotalCarrito(): 
    mostrarLeyendaDescuento()
    mostrarLeyendaEnvio()
    subtotal = 0
    cantidadProd = 0
    descuento = 0
    for producto in Carrito.keys():
        cantidadProd += 1
        subtotal += Carrito[producto]['precioLista']
        descuento += calcularDescuento(producto)
    envio = calcularEnvio(subtotal,cantidadProd)
    total = subtotal - descuento + envio
    print(f'''
    Total de Productos vendidos: {cantidadProd}
    Subtotal: {subtotal}
    Descuento adquirido: {descuento}
    Costo de envio: {envio}
    ----
    Total a pagar: {total}
    ''')
        
def validarSKUExistente(sku):
    prod = isSKUExistente(sku)
    if not prod:
        raise Exception("No se encuentra SKU ", sku)    
    return prod
    
def isSKUExistente(sku):
    for productos in Articulos.values():
        d = productos.get(sku,None)
        if not d == None:
            return d
    return None


def solicitarCantidad(sku,productoSKU):
    while True:
        print (f"Ingrese la cantidad por llevar. La cantidad disponible para el SKU {sku} es: {productoSKU['inventario']} ")
        tam = int(input())
        if  tam > productoSKU['inventario']:
            print(f"Cantidad no disponible")
        if tam == 0:
            print("Cantidad no puede ser 0")
        else:
            return tam
        
def solicitarColor(sku,productoSKU):
    return solicitarX(sku,productoSKU,"color", "color","colores")


def solicitarTamano(sku,productoSKU):
    return solicitarX(sku,productoSKU,"tamano", "tamaño","tamaños")


def solicitarX(sku,productoSKU, X, Xd,Xs):
    while True:
        print (f"Ingrese un {Xd}. Los {Xs} disponibles para el SKU {sku} son:")
        print (unpackList(productoSKU[X]) )
        tam = input()
        if not tam in productoSKU[X]:
            print(f"{X} no disponible")
        else:
            return tam
    
## ======= MAIN    
FIN = 0
            
crearCategorias()
#imprimirCategorias()
#mostrarCategoriasDisponibles()
 

while True:    
    mostrarMenu()
    try:
        opcion = solicitarOpcion()
        
    except:
        print ("Opcion invalida, vuelva a intentarlo")
        continue
    
    if opcion == OPCIONES_MENU["SALIR"]:
        break
    
    ejecutarOpcion(opcion)
    
print ("Hasta Luego")