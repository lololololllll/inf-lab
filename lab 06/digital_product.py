
from product import Product, ProductRecord
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(
        self, product_id: str, name: str, price: float, stock: int,
        download_size: float, supplier: Supplier,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> ProductRecord:
        return {
            "type": "digital",
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "download_size": self.download_size,
            "supplier": self.supplier.to_dict(),
        }
