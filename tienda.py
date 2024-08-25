#atributos
# Cada tienda creada, independiente de su tipo, posee un nombre, un listado de
# productos y un costo de delivery

#metodo
# Al momento de crear una nueva tienda, se debe
# solicitar el nombre y el costo de delivery (todas las tiendas se crean inicialmente sin
# productos) . En una tienda ya existente, no se puede modificar el nombre ni el costo dedelivery

from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    products = []
    @abstractmethod
    def __init__(self, name:str, delivery_cost:int):
        self.__name = name
        self.__delivery = delivery_cost

    @abstractmethod
    def add_product(self, Producto):
        pass

    @abstractmethod
    def product_list(self, productos):
        pass

    @abstractmethod
    def sell_product(self, Producto, productos):
        pass


class Restaurant(Tienda):
    def __init__(self, name: str, delivery_cost: int):
        super().__init__(name, delivery_cost)
        self.__name = name
        self.__delivery = delivery_cost
        self.products = Tienda.products

    @property
    def name(self):
        return self.__name
    @property
    def delivery(self):
        return self.__delivery
    
    def add_product(self, Producto):
        Producto.stock = 0
        self.products.append(Producto)
        pass
    
    def product_list(self):
        print("--------------------")
        for i in self.products:
            print(f"Nombre producto : {i.name} \nPrecio producto : {i.price}")
            print("--------------------")

    def sell_product(self,product_to_sell, quantity = 0):
        index = self.check_product(product_to_sell)
        if index != None:
            if self.products[index].stock >= quantity:
                self.products[index].stock -= quantity
        else:
            print("No hay productos para vender")
        pass

    def check_product(self,product_to_sell:str):
        index = 0
        for i in self.products:
            if i.name == product_to_sell:
                break
            index +=1
        return index



class Supermercado(Tienda):
    def __init__(self, name: str, delivery_cost: int):
        super().__init__(name, delivery_cost)
        self.__name = name
        self.__delivery = delivery_cost
        self.products = Tienda.products

    @property
    def name(self):
        return self.__name
    @property
    def delivery(self):
        return self.__delivery
    
    def add_product(self, Producto):
        self.products.append(Producto)
        pass
    
    def product_list(self):
        print("--------------------")
        for i in self.products:
            print(f"Nombre producto : {i.name} \nPrecio producto : {i.price} ")
            if i.stock < 10 :
                print(f"Pocos productos disponibles\nStock producto : {i.stock}")
            print("--------------------")

    def sell_product(self,product_to_sell, quantity = 0):
        index = self.check_product(product_to_sell)
        if index != None:
            if self.products[index].stock >= quantity:
                self.products[index].stock -= quantity
        else:
            print("No hay productos para vender")
        pass

    def check_product(self,product_to_sell:str):
        index = 0
        for i in self.products:
            if i.name == product_to_sell:
                break
            index +=1
        return index


class Farmacia(Tienda):
    def __init__(self, name: str, delivery_cost: int):
        super().__init__(name, delivery_cost)
        self.__name = name
        self.__delivery = delivery_cost
        self.products = Tienda.products

    @property
    def name(self):
        return self.__name
    @property
    def delivery(self):
        return self.__delivery
    
    def add_product(self, Producto):
        self.products.append(Producto)
        pass
    
    def product_list(self):
        print("--------------------")
        for i in self.products:
            print(f"Nombre producto : {i.name} \n ")
            if i.price > 150000 :
                print(f"Envío gratis al solicitar este producto")
            print(f"Precio producto : {i.price}")
            print("--------------------")

    def sell_product(self,product_to_sell, quantity = 0):
        index = self.check_product(product_to_sell)
        if quantity > 3:
            print("El maximo de unidades por usuario es 3")
            quantity = 3
        if index != None:
            if self.products[index].stock >= quantity:
                self.products[index].stock -= quantity
        else:
            print("No hay suficientes productos para vender")
        pass

    def check_product(self,product_to_sell:str):
        index = 0
        for i in self.products:
            if i.name == product_to_sell:
                break
            index +=1
        return index





if __name__ == '__main__':
    r = Restaurant("Mc",1000)
    opcion_ingreso = 1
    while opcion_ingreso == 1:
        nombre= str(input("Ingrese el nombre del producto       : "))
        precio = float(input("Ingrese el precio del producto        :"))
        stock = int(input("Ingrese el stock del producto       :"))
        p = Producto(nombre, precio,stock)
        if p in r.products:
            indice = r.products.index(p)
            r.products[indice] += p
        else:
            r.add_product(p)
        opcion_ingreso = int(input("0 para terminar 1 continuar:"))
    r.sell_product("qwe",2)
    r.product_list()
    # r.sell_product("qwe",3)

