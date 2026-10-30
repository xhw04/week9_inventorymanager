# STORE PRODUCT
# ADD PRODUCT
# SEARCH PRODUCT
# DISPLAY PRODUCT

# create class
class Inventory:
    def __init__(self):
        # products is list
        self.__products = []

# get products from list
    def get_products(self):
        return self.__products

# 1.display all products from list
    def display_all(self):
        print("\nCurrent Inventory:")
        print("------------------")
        # call list
        for product in self.__products:
            # call product.py
            product.display_information()
        print("------------------")


# 4.search from dict

    def search_product(self, product_id):
        # from list
        for product in self.__products:
            # call product.py
            if product.get_product_id() == product_id:
                return product
        return None

# 2.add from dict
    def add_product(self, product):
        # call product.py,if not empty
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return False
        # then append to list
        self.__products.append(product)
        return True
