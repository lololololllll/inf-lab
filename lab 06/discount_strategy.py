from abc import ABC, abstractmethod
from math import isfinite


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        if not isfinite(percentage) or not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        if not isfinite(threshold) or not isfinite(amount) or threshold < 0 or amount < 0:
            raise ValueError("Threshold and amount must be finite and non-negative.")
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        return max(0.0, total - self.amount) if total >= self.threshold else total


class StudentDiscount(PercentageDiscount):
    """A fourth strategy with a fixed student discount of 5 percent."""
    def __init__(self) -> None:
        super().__init__(5)
