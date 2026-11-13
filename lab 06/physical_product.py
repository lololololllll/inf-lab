from can_be_shipped import CanBeShipped
from product import Product, ProductRecord
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self, product_id: str, name: str, price: float, stock: int,
        weight: float, supplier: Supplier,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight} kg")
        print(f"Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 5 + self.weight * 2

    def to_dict(self) -> ProductRecord:
        return {
            "type": "physical",
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "weight": self.weight,
            "supplier": self.supplier.to_dict(),
        }
