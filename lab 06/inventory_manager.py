import json
import os

inventory= [
    {
        "Id" : "P001",
        "Name" : "Laptop",
        "price" :  1200,
        "stock" : 15
    },
    {
        "Id" : "P002",
        "Name" :  "Mouse",
        "price" : 25.50,
        "stock" : 40
    },
    {
        "Id" : "P003",
        "Name" :  "Keyboard",
        "price" :  45.00,
        "stock" : 25
    }
]


def load_inventory():
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


def display_all(inventory):
    print("\nCurrent Inventory")
    print("--------------------------------")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    for product in inventory:
        print(
            "ID:", product["id"],
            "| Name:", product["name"],
            "| Price: $" + format(product["price"], ".2f"),
            "| Stock:", product["stock"]
        )

    print("--------------------------------")


def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock quantity.")
        return

    product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    print("Product added successfully!")

def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"].lower() == product_id.lower():

            print("\nProduct Found")
            print("--------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price: $" + format(product["price"], ".2f"))
            print("Stock:", product["stock"])
            print("--------------------------------")

            return

    print("Product not found.")

def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:

        if product["id"].lower() == product_id.lower():

            print("\nProduct Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            try:
                new_stock = int(input("\nNew Stock Quantity: "))
            except ValueError:
                print("Invalid stock quantity.")
                return

            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")


def display_menu():
    print("\n---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")   

inventory = load_inventory()

while True:

    display_menu()

    option = input("\nEnter option: ")

    if option == "1":
        display_all(inventory)

    elif option == "2":
        add_product(inventory)

    elif option == "3":
        update_stock(inventory)

    elif option == "4":
        search_product(inventory)

    elif option == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)

    elif option == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)

        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please select 1 to 6.")