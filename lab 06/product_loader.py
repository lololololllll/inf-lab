import csv
from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="", encoding="utf-8-sig")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            rows = csv.reader(file)
            next(rows, None)
            for row_number, row in enumerate(rows, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError("Expected five CSV columns.")
                    kind, product_id, name, price, stock = (cell.strip() for cell in row)
                    if inventory.find_product(product_id) is not None:
                        raise ValueError(f"Duplicate product ID: {product_id}")
                    product = ProductFactory.create(kind, product_id, name, float(price), int(stock), supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
