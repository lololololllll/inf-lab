
import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct


class Inventory:
    def __init__(self, filename="inventory.json"):
        self.products = []
        self.filename = filename
        self.load_inventory()

    def display_all(self):
        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            print("--------------------")
            product.display_information()
            print(product.get_fulfilment_info())

            if isinstance(product, PhysicalProduct):
                print(
                    f"Shipping Cost: "
                    f"${product.calculate_shipping_cost():.2f}"
                )

    def add_product(self, product):
        if self.search_product(product.product_id) is not None:
            print("Product ID already exists.")
            return

        self.products.append(product)
        print("Product added successfully.")

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)

        if product is None:
            print("Product not found.")
            return

        if product.update_stock(quantity):
            print("Stock updated successfully.")

    def save_inventory(self):
        data = [product.to_dict() for product in self.products]

        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

            print("Inventory saved successfully.")
        except OSError as error:
            print(f"Error saving inventory: {error}")

    def load_inventory(self):
        if not os.path.exists(self.filename):
            print("No existing inventory file found.")
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
            print("Loading file:", os.path.abspath(self.filename))
            print("JSON data:", data)
            print("Number of products:", len(data))

            for item in data:
                if item["type"] == "physical":
                    product = PhysicalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["weight"]
                    )

                elif item["type"] == "digital":
                    product = DigitalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"]
                    )

                else:
                    print("Unknown product type skipped.")
                    continue

                self.products.append(product)

            print("Inventory loaded successfully.")

        except (OSError, ValueError, KeyError, TypeError) as error:
            self.products = []
            print(f"Error loading inventory: {error}")
