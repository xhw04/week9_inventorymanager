# -FILE HANDLING-
# loading inventory.json
# saving inventory.json

# -MAIN-
# displaying the main menu
# 1. Display all products
# 2. Add a product
# 3. Update stock
# 4. Search for a product
# 5. Save inventory
# 6. Exit

# asking the user for input (encapsulation called method)
# managing the entire inventory


import json
import os
from product import Product
from inventory import Inventory

file_name = "inventory.json"


# 5.save

# call json dict from product.py
def save_inventory(inventory):
    # call product list from inventory.py
    data = [p.to_dict() for p in inventory.get_products()]
    with open(file_name, "w")as file:
        json.dump(data, file, indent=4)

# 1.display (load)


def load_inventory():
    inventory = Inventory()
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        for item in data:
            # call inventory.py to load list
            inventory.add_product(
                Product(item["ID"], item["Name"], item["Price"], item["Stock"]))
            print("inventory.json found.Inventory loaded successfully.")
    else:
        print("inventory.json not found.Creating default inventory.")
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 25))
        save_inventory(inventory)
    return inventory

# 2.add product


def add_product_menu(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid number entered.")
        return
    if inventory.add_product(Product(product_id, name, price, stock)):
        print("\nProduct added successfully!")

# 3.update


def update_stock_menu(inventory):
    print("\nUpdate Stock")
    product = inventory.search_product(input("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    product.display_information()
    try:
        quantity = int(input("New Stock Quantity: "))
    except ValueError:
        print("Invalid number entered.")
        return
    if product.update_stock(quantity):
        print("\nStock updated successfully!")

# 4.search product


def search_product_menu(inventory):
    print("\nSearch Product")
    product = inventory.search_product(input("Enter Product ID: "))
    if product is None:
        print("Product not found.")
    else:
        print("Product Found")
        product.display_information()


def main():
    print("============")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("============\n")
    inventory = load_inventory()

    while True:
        print("\n-----------MENU------------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("---------------------------")

        try:
            choice = int(input("Enter option: "))
        except ValueError:
            print("Please enter a number 1-6.")
            continue

        if choice == 1:
            inventory.display_all()
        elif choice == 2:
            add_product_menu(inventory)
        elif choice == 3:
            update_stock_menu(inventory)
        elif choice == 4:
            search_product_menu(inventory)
        elif choice == 5:
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif choice == 6:
            save_inventory(inventory)
            print("Inventory saved. Thank you for using Inventory Management System.")
            break
        else:
            print("Invalid option.")


# call main
main()
