# create class,represent and manage product
# __product_id:String
# __name:String
# __price:float
# __stock:int

# update_stock(quantity:int)void
# display_information():void

# -PRODUCT-
# STORE PRODUCT INFO
# MANAGE STATE

class Product:
    # from previous, have id/name/price/stock-parameters
    # self.__ (private attributes,only in class)
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

# class-object(passed from main)-parameter-attribute

# inventory-private
    def get_product_id(self):
        return self.__product_id

# 1.display one row of product info(id,name,stock,price)
    def display_information(self):
        print(f"ID:{self.__product_id} | Name:{self.__name} |"
              f"Price:${self.__price:} | Stock:{self.__stock}"
              )

# 3.update stock (encapsulation)
    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative.")
            return False
        self.__stock = quantity
        return True

# return as dict due to json (only here)
    def to_dict(self):
        return {"ID": self.__product_id, "Name": self.__name,
                "Price": self.__price, "Stock": self.__stock}
