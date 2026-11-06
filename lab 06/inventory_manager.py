
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


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
        print("\n1. Physical Product")
        print("2. Digital Product")

        product_type = input("Choose product type: ")

        if product_type not in ("1", "2"):
            print("Invalid product type.")
            continue

        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")

        try:
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))

            if price < 0 or stock < 0:
                print("Price and stock cannot be negative.")
                continue

            if product_type == "1":
                weight = float(input("Enter Weight (kg): "))

                if weight < 0:
                    print("Weight cannot be negative.")
                    continue

                product = PhysicalProduct(
                    product_id, name, price, stock, weight
                )

            else:
                download_size = float(
                    input("Enter Download Size (MB): ")
                )

                if download_size < 0:
                    print("Download size cannot be negative.")
                    continue

                product = DigitalProduct(
                    product_id, name, price, stock, download_size
                )

            inventory.add_product(product)

        except ValueError:
            print("Invalid number entered.")

    elif choice == "3":
        product_id = input("Enter Product ID: ")

        try:
            quantity = int(
                input("Enter stock change (+ to add, - to remove): ")
            )
            inventory.update_stock(product_id, quantity)

        except ValueError:
            print("Invalid quantity.")

    elif choice == "4":
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product:
            product.display_information()
            print(product.get_fulfilment_info())

            if isinstance(product, PhysicalProduct):
                print(
                    f"Shipping Cost: "
                    f"${product.calculate_shipping_cost():.2f}"
                )
        else:
            print("Product not found.")

    elif choice == "5":
        inventory.save_inventory()

    elif choice == "6":
        inventory.save_inventory()
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
