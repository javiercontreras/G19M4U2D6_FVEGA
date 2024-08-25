

#, pero sí se puede modificar los productos (mediante el ingreso de un producto,
#o mediante la realización de ventas).

#Todas las tiendas deben poder ingresar un producto, listar los productos existentes, y
#realizar ventas
from tienda import Restaurant, Supermercado, Farmacia
from producto import Producto
b_listar_productos = True
b_vender_productos = True

print("Administrador bienvenido a la creacion de su tienda")
tipo = int(input("\nEliga el tipo de tienda:\n"
"1. Restaurant\n"
"2. Farmacia\n"
"3. Supermercado\n"))
nombre_tienda= str(input("\nIngrese el nombre de su tienda:\n"))
costo_delivery = int(input("\nIngrese el costo del delivery:\n"))
if tipo == 1:
    tienda = Restaurant(nombre_tienda, costo_delivery)
elif tipo == 2:
    tienda = Farmacia(nombre_tienda, costo_delivery)
elif tipo == 3:
    tienda = Supermercado(nombre_tienda, costo_delivery)

while b_listar_productos:
    option_user_sell = int(input("\nEliga entre agregar o salir:\n"
    "1. Listar los productos existentes\n"
    "2. Agregar item\n"
    "3. Pasar a gestion Tienda\n"))
    if option_user_sell == 1: #listar
        tienda.product_list()
    elif option_user_sell == 2: #agregar
        nombre= str(input("Ingrese el nombre del producto       : "))
        precio = float(input("Ingrese el precio del producto        :"))
        stock = int(input("Ingrese el stock del producto       :"))
        p = Producto(nombre, precio, stock)
        if p in tienda.products:
            indice = tienda.products.index(p)
            tienda.products[indice] += p
        else:
            tienda.add_product(p)
    elif option_user_sell == 3: #salir
        b_listar_productos = False
    
    
    

while b_vender_productos:
    print("\nQue accion desea realizar")
    option_user_sell = int(input("\nEliga el tipo de tienda:\n"
    "1. Listar los productos existentes\n"
    "2. Realizar una venta\n"
    "3. Salir programa\n"))
       
    if option_user_sell == 1: #listar
        tienda.product_list()
        pass
    elif option_user_sell == 2: #vender
        nombre_sell= str(input("Ingrese el nombre del producto       : "))
        quantity_sell = int(input("Ingrese la cantidad del producto a comprar    :"))
        tienda.sell_product(nombre_sell, quantity_sell)

    elif option_user_sell == 3:
        b_vender_productos = False