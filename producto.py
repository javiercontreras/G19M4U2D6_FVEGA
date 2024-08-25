# Los productos tienen un nombre, un precio y un stock. Los 3 valores se deben solicitar
# al momento de crear un producto nuevo, pero si no se indica stock, se asume que es
# 0. No se puede modificar el nombre ni el precio de un producto, solo su stock. Si se
# intenta modificar el stock por un valor menor a 0, se debe asignar 0 en su lugar. De
# cada producto se puede obtener su nombre, su precio o su stock.

class Producto():
    def __init__(self, name:str, price:float, stock = 0):
        self.__name = name
        self.__price = self.validate_price(price)
        self.__stock = self.validate_stock(stock)

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        self.__stock = self.validate_stock(new_stock)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __eq__(self,other):
        return self.name.lower() == other.name.lower()
    
    def __iadd__(self, other):
        if self == other:
            self.stock += other.stock
        return self
    
    def __isub__(self, other):
        if self == other:
            self.stock -= other.stock
        return self
    
    
    def validate_price(self, new_price):
        if new_price >= 0:
            return new_price
        else:
            raise ValueError("Price must be non-negative.")

    def validate_stock(self, new_stock):
        if new_stock>= 0:
            return new_stock
        else:
            return 0
        
    

if __name__ == '__main__':
    nombre= str(input("Ingrese el nombre del producto       : "))
    precio = float(input("Ingrese el precio del producto        :"))
    stock = int(input("Ingrese el stock del producto       :"))
    p = Producto(nombre, precio, stock)
    
    