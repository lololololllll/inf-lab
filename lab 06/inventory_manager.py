from pathlib import Path
from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from product_factory import ProductFactory
from product_loader import load_products
from input_helpers import get_positive_float, get_integer
from inventory import Inventory
from order import Order
from product import Product
from supplier import Supplier


def read_supplier(inventory: Inventory) -> Supplier:
    supplier_id = input("Enter Supplier ID: ").strip()
    if not supplier_id:
        raise ValueError("Supplier ID is required.")
    for product in inventory.products:
        if product.supplier.supplier_id == supplier_id:
            return product.supplier
    name = input("Enter Supplier Name: ").strip()
    email = input("Enter Supplier Email: ").strip()
    if not name or not email:
        raise ValueError("Supplier name and email are required.")
    return Supplier(supplier_id, name, email)


def add_product(inventory: Inventory) -> None:
    product_type = input("\n1. Physical Product\n2. Digital Product\nChoose product type: ")
    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return
    product_id = input("Enter Product ID: ").strip()
    name = input("Enter Product Name: ").strip()
    price = get_positive_float("Enter Price: ")
    stock = get_integer("Enter Stock Quantity: ", 0)
    if price < 0 or stock < 0:
        raise ValueError("Price and stock cannot be negative.")
    product: Product
    if product_type == "1":
        weight = float(input("Enter Weight (kg): "))
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        product = ProductFactory.create("physical", product_id, name, price, stock, read_supplier(inventory), weight=weight)
    else:
        size = float(input("Enter Download Size (MB): "))
        if size < 0:
            raise ValueError("Download size cannot be negative.")
        product = ProductFactory.create("digital", product_id, name, price, stock, read_supplier(inventory), download_size=size)
    inventory.add_product(product)


def build_order(inventory: Inventory) -> None:
    order = Order(input("Enter Order ID: ").strip())
    while product_id := input("Enter Product ID (blank to finish): ").strip():
        product = inventory.find_product(product_id)
        if product is None:
            print("Product not found.")
            continue
        try:
            order.add_order_line(product, get_integer("Enter Quantity: ", 1))
        except ValueError as error:
            print(error)
    strategies = {"1": NoDiscount(), "2": PercentageDiscount(10),
                  "3": BulkDiscount(200, 20), "4": StudentDiscount()}
    while True:
        choice = input("Discount: 1 None / 2 Ten percent / 3 Bulk / 4 Student: ")
        if choice in strategies:
            order.set_discount(strategies[choice])
            break
        print("Invalid discount choice.")
    print(f"Order {order.order_id}")
    for line in order.order_lines:
        print(f"{line.product.name} x {line.quantity}: ${line.calculate_subtotal():.2f}")
    print(f"Total: ${order.calculate_total():.2f}")


def main() -> None:
    inventory = Inventory()
    while True:
        print(
            "\n===== INVENTORY MANAGEMENT SYSTEM =====\n"
            "1. Display all products\n2. Add product\n3. Update stock\n"
            "4. Search product\n5. Save inventory\n6. Exit\n"
            "7. Remove product\n8. Calculate order total\n9. Load products from CSV"
        )
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                inventory.display_all_products()
            elif choice == "2":
                add_product(inventory)
            elif choice == "3":
                product_id = input("Enter Product ID: ")
                quantity = int(input("Enter stock change (+ to add, - to remove): "))
                inventory.update_stock(product_id, quantity)
            elif choice == "4":
                product = inventory.find_product(input("Enter Product ID: "))
                if product is None:
                    print("Product not found.")
                else:
                    product.display_information()
                    print(product.get_fulfilment_info())
                    product.supplier.display_information()
            elif choice == "5":
                inventory.save_inventory()
            elif choice == "6":
                print("Exiting program.")
                return
            elif choice == "7":
                inventory.remove_product(input("Enter Product ID: "))
            elif choice == "8":
                build_order(inventory)
            elif choice == "9":
                path = input("CSV path (blank for products.csv): ").strip()
                path = path or str(Path(__file__).with_name("products.csv"))
                supplier = Supplier("CSV", "CSV Supplier", "csv@example.com")
                load_products(path, inventory, supplier)
            else:
                print("Invalid choice. Please try again.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
