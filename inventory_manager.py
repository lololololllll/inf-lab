import json
import os

inventory= [
    {
        "Id :" == "P001",
        "Name :" == "Laptop",
        "price :" == 1200,
        "stock :" == 15
    },
    {
        "Id :" == "P002",
        "Name :" == "Mouse",
        "price :" == 25.50,
        "stock :" == 40
    },
    {
        "Id :" == "P003",
        "Name :" == "Keyboard",
        "price :" == 45.00,
        "stock :" == 25
    }
]


def load_inventory():
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")
