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

from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


class Product(ABC):
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

    @abstractmethod
    def get_fulfilment_info(Self):
        pass

# child class(inheritance)


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        # super
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight:{self.__weight}kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping"

    def calculate_shipping_cost(self):
        return self.__weight * 2.5

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "physical"
        data["Weight"] = self.__weight
        return data


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size:{self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "digital"
        data["Download_size"] = self.__download_size
        return data
