
from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        return {
            "type": "digital",
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "download_size": self.download_size
        }
