
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock + quantity < 0:
            print("Not enough stock.")
            return False

        self.stock += quantity
        return True

    def display_information(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
