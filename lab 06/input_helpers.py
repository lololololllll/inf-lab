from math import isfinite


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if not isfinite(value) or value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def get_integer(prompt: str, minimum: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter an integer of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")
