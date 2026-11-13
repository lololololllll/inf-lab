from abc import ABC, abstractmethod
from typing import NotRequired, TypedDict

from supplier import Supplier, SupplierRecord


class ProductRecord(TypedDict):
    type: str
    id: str
    name: str
    price: float
    stock: int
    supplier: NotRequired[SupplierRecord]
    weight: NotRequired[float]
    download_size: NotRequired[float]


class Product(ABC):
    def __init__(
        self, product_id: str, name: str, price: float, stock: int, supplier: Supplier
    ) -> None:
        self.product_id: str = product_id
        self.name: str = name
        self.price: float = price
        self.stock: int = stock
        self.supplier: Supplier = supplier

    def update_stock(self, quantity: int) -> bool:
        if self.stock + quantity < 0:
            print("Not enough stock.")
            return False
        self.stock += quantity
        return True

    def display_information(self) -> None:
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> ProductRecord:
        pass
