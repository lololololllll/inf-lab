from dataclasses import dataclass
from discount_strategy import DiscountStrategy, NoDiscount
from product import Product


@dataclass(frozen=True)
class OrderLine:
    product: Product
    quantity: int

    def __post_init__(self) -> None:
        if not isinstance(self.quantity, int) or isinstance(self.quantity, bool) or self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero and an integer.")

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id = order_id
        self._order_lines: list[OrderLine] = []
        self.discount = NoDiscount() if discount is None else discount

    @property
    def order_lines(self) -> tuple[OrderLine, ...]:
        return tuple(self._order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        self._order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, index: int) -> None:
        del self._order_lines[index]

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def calculate_total(self) -> float:
        total = sum((line.calculate_subtotal() for line in self._order_lines), 0.0)
        return self.discount.apply(total)
