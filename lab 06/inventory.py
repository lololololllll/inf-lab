
from product import Product

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
