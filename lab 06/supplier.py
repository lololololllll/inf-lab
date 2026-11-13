from dataclasses import dataclass
from typing import TypedDict


class SupplierRecord(TypedDict):
    supplier_id: str
    name: str
    contact_email: str


@dataclass(frozen=True)
class Supplier:
    supplier_id: str
    name: str
    contact_email: str

    def display_information(self) -> None:
        print(f"Supplier: {self.name} ({self.supplier_id})")
        print(f"Contact Email: {self.contact_email}")

    def to_dict(self) -> SupplierRecord:
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "contact_email": self.contact_email,
        }
