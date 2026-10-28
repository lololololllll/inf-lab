
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

                
if __name__ == "__main__":
    inventory = Inventory()

    product1 = Product("P001", "Laptop", 1200.00, 15)
    product2 = Product("P002", "Mouse", 25.50, 40)

    inventory.add_product(product1)
    inventory.add_product(product2)

    inventory.display_all()