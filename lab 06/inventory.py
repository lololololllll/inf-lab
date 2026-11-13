import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product import Product, ProductRecord
from supplier import Supplier


LEGACY_SUPPLIER = Supplier("UNASSIGNED", "Supplier not recorded", "")


class Inventory:
    def __init__(self, filename: str | None = None) -> None:
        self.products: list[Product] = []
        self.filename: str = (
            str(Path(__file__).with_name("inventory.json"))
            if filename is None
            else filename
        )
        self.load_inventory()

    def display_all_products(self) -> None:
        if not self.products:
            print("Inventory is empty.")
        for product in self.products:
            print("--------------------")
            product.display_information()
            print(product.get_fulfilment_info())

    def display_all(self) -> None:
        self.display_all_products()

    def add_product(self, product: Product) -> None:
        if self.find_product(product.product_id) is not None:
            print("Product ID already exists.")
            return
        self.products.append(product)
        print("Product added successfully.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product is None:
            print("Product not found.")
            return
        self.products.remove(product)
        print("Product removed successfully.")

    def update_stock(self, product_id: str, quantity: int) -> None:
        product = self.find_product(product_id)
        if product is None:
            print("Product not found.")
        elif product.update_stock(quantity):
            print("Stock updated successfully.")

    def save_inventory(self) -> None:
        path = Path(self.filename)
        data = [product.to_dict() for product in self.products]
        temp_path: Path | None = None
        try:
            with NamedTemporaryFile(
                mode="w", encoding="utf-8", dir=path.parent,
                prefix=path.name + ".", suffix=".tmp", delete=False,
            ) as file:
                temp_path = Path(file.name)
                json.dump(data, file, indent=4)
                file.write("\n")
            temp_path.replace(path)
            temp_path = None
            print("Inventory saved successfully.")
        except OSError as error:
            print(f"Error saving inventory: {error}")
        finally:
            if temp_path is not None:
                temp_path.unlink(missing_ok=True)

    def load_inventory(self) -> None:
        try:
            data: list[ProductRecord] = json.loads(
                Path(self.filename).read_text(encoding="utf-8-sig")
            )
            products: list[Product] = []
            suppliers: dict[Supplier, Supplier] = {LEGACY_SUPPLIER: LEGACY_SUPPLIER}
            for item in data:
                supplier_data = item.get("supplier")
                supplier = Supplier(**supplier_data) if supplier_data else LEGACY_SUPPLIER
                supplier = suppliers.setdefault(supplier, supplier)
                details = item["id"], item["name"], item["price"], item["stock"]
                if item["type"] == "physical":
                    products.append(PhysicalProduct(*details, item["weight"], supplier))
                elif item["type"] == "digital":
                    products.append(DigitalProduct(*details, item["download_size"], supplier))
                else:
                    print("Unknown product type:", item["type"])
            self.products = products
        except FileNotFoundError:
            print(f"Inventory file not found: {Path(self.filename).resolve()}")
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
            print("Error loading inventory:", error)
