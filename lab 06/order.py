from dataclasses import dataclass

from product import Product


@dataclass(frozen=True)
class OrderLine:
    product: Product
    quantity: int

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self._order_lines: list[OrderLine] = []

    @property
    def order_lines(self) -> tuple[OrderLine, ...]:
        return tuple(self._order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Order quantity must be positive.")
        self._order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, index: int) -> None:
        del self._order_lines[index]

    def calculate_total(self) -> float:
        return sum((line.calculate_subtotal() for line in self._order_lines), 0.0)
