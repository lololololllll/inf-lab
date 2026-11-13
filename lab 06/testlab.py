import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from digital_product import DigitalProduct
from inventory import Inventory, LEGACY_SUPPLIER
from order import Order
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


class Lab8Tests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name)

    def make_products(self, supplier: Supplier) -> tuple[PhysicalProduct, DigitalProduct]:
        return (
            PhysicalProduct("P1", "Mouse", 25.0, 10, 0.2, supplier),
            DigitalProduct("D1", "Antivirus", 30.0, 20, 500.0, supplier),
        )

    def test_association_survives_deleting_supplier_variable(self) -> None:
        supplier = Supplier("S1", "Example Supplies", "sales@example.com")
        physical, digital = self.make_products(supplier)
        self.assertIs(physical.supplier, supplier)
        self.assertIs(digital.supplier, supplier)
        del supplier
        physical.supplier.display_information()
        digital.supplier.display_information()
        self.assertIs(physical.supplier, digital.supplier)
        self.assertIsNot(physical, physical.supplier)
        self.assertEqual(physical.supplier.contact_email, "sales@example.com")

    def test_aggregation_transfers_existing_product(self) -> None:
        product, _ = self.make_products(LEGACY_SUPPLIER)
        inventory_a = Inventory(str(self.folder / "a.json"))
        inventory_b = Inventory(str(self.folder / "b.json"))
        inventory_a.add_product(product)
        self.assertIs(inventory_a.find_product("P1"), product)
        inventory_a.remove_product("P1")
        self.assertIsNone(inventory_a.find_product("P1"))
        self.assertTrue(product.update_stock(2))
        inventory_b.add_product(product)
        self.assertIs(inventory_b.find_product("P1"), product)
        self.assertEqual(product.stock, 12)

    def test_composition_creates_separate_order_lines(self) -> None:
        physical, digital = self.make_products(LEGACY_SUPPLIER)
        order_a = Order("A")
        order_b = Order("B")
        order_a.add_order_line(physical, 2)
        order_a.add_order_line(digital, 1)
        order_b.add_order_line(physical, 1)
        for line in order_a.order_lines:
            print(f"{line.product.name} x {line.quantity} = ${line.calculate_subtotal():.2f}")
        self.assertEqual(order_a.calculate_total(), 80.0)
        self.assertIsNot(order_a.order_lines[0], order_b.order_lines[0])
        self.assertIs(order_a.order_lines[0].product, order_b.order_lines[0].product)
        order_a.remove_order_line(0)
        self.assertEqual(order_a.calculate_total(), 30.0)
        self.assertEqual(order_b.calculate_total(), 25.0)
        self.assertIs(order_b.order_lines[0].product, physical)
        with self.assertRaises(ValueError):
            order_a.add_order_line(physical, 0)

    def test_lsp_and_polymorphism_through_product_references(self) -> None:
        inventory = Inventory(str(self.folder / "products.json"))
        for product in self.make_products(LEGACY_SUPPLIER):
            inventory.add_product(product)
        output = io.StringIO()
        with redirect_stdout(output):
            for product in inventory.products:
                show_product_details(product)
            inventory.display_all_products()
        display = output.getvalue()
        print(display, end="")
        for expected in (
            "Weight: 0.2 kg",
            "Download Size: 500.0 MB",
            "This product requires physical shipping.",
            "This product is delivered digitally.",
        ):
            self.assertEqual(display.count(expected), 2)
        for product in inventory.products:
            starting_stock = product.stock
            inventory.update_stock(product.product_id, 3)
            self.assertEqual(product.stock, starting_stock + 3)
            self.assertTrue(product.update_stock(-2))
            self.assertFalse(product.update_stock(-100))
            self.assertEqual(product.stock, starting_stock + 1)

    def test_legacy_inventory_and_supplier_round_trip(self) -> None:
        path = self.folder / "products.json"
        path.write_text(
            '[{"type":"physical","id":"OLD1","name":"Laptop",'
            '"price":1200.0,"stock":15,"weight":2.0}]',
            encoding="utf-8",
        )
        inventory = Inventory(str(path))
        self.assertEqual(len(inventory.products), 1)
        self.assertIs(inventory.products[0].supplier, LEGACY_SUPPLIER)
        supplier = Supplier("S1", "Example Supplies", "sales@example.com")
        for product in self.make_products(supplier):
            inventory.add_product(product)
        inventory.save_inventory()
        loaded = Inventory(str(path))
        self.assertEqual(len(loaded.products), 3)
        first, second = loaded.products[-2:]
        self.assertEqual(first.supplier, supplier)
        self.assertIs(first.supplier, second.supplier)
        self.assertEqual(first.get_fulfilment_info(), "This product requires physical shipping.")
        self.assertEqual(second.get_fulfilment_info(), "This product is delivered digitally.")


if __name__ == "__main__":
    unittest.main()
