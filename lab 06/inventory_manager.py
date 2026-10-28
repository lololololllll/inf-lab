
from product import Product
from inventory import Inventory

inventory = Inventory()

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Display all products")
    print("2. Add product")
    print("3. Update stock")
    print("4. Search product")
    print("5. Save inventory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display_all()

    elif choice == "2":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")

        try:
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))

            if inventory.search_product(product_id):
                print("Product ID already exists.")

            elif price < 0 or stock < 0:
                print("Price and stock cannot be negative.")

            else:
                product = Product(product_id, name, price, stock)
                inventory.add_product(product)

        except ValueError:
            print("Invalid price or stock.")

    elif choice == "3":
        product_id = input("Enter product ID: ")
        product = inventory.search_product(product_id)

        if product:
            try:
                quantity = int(input("Enter new stock: "))
                product.update_stock(quantity)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Enter product ID: ")
        product = inventory.search_product(product_id)

        if product:
            product.display_information()
        else:
            print("Product not found.")

    elif choice == "5":
        print("Save function will be added in Step 4.")

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
