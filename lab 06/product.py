from abc import ABC, abstractmethod
from math import isfinite
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
        self.price = price
        self.stock = stock
        self.supplier: Supplier = supplier

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if not isfinite(value) or value <= 0:
            raise ValueError("Price must be a finite number greater than zero.")
        self._price = value

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Stock quantity must be a non-negative integer.")
        self._stock = value

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
