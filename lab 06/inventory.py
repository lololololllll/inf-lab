
from product import Product
import json

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully.")

    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if len(self.products) == 0:
            print("Inventory is empty.")
        else:
            for product in self.products:
                product.display_information()

    # NEW: Load products from JSON
    def load_inventory(self):
        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

            self.products = []

            for item in data:
                product = Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
                self.products.append(product)

            print("Inventory loaded successfully.")

        except FileNotFoundError:
            print("Inventory file not found.")

    # NEW: Save products to JSON
    def save_inventory(self):
        data = []

        for product in self.products:
            data.append(product.to_dict())

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully.")
