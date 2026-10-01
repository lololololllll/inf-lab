def get_valid_input():
    stock = input("Enter delivery amount or 'quit' to exit: ")

    if stock.lower() == 'quit':
        return "quit"

    if stock.startswith("-"):
        print("Invalid input. Please enter a positive number.")
        return None

    if not stock.isdigit():
        print("Invalid input. Please enter a valid number.")
        return None 


    return int(stock)

def process_delivery_(current_total , new_value ):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_entries):
    print("Total inventory:", total_units)
    print("Failed entries:", failed_entries)

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            inventory = int(lines[0].strip())

            history = []

            if len(lines) > 1:
                history_text = lines[1].strip()

                if history_text:
                    history = [int(value) for value in history_text.split(",")]

            return inventory, history

    except FileNotFoundError:
        return 0, []


def save_inventory(inventory, history):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory) + "\n")

        history_text = ",".join(str(value) for value in history)

        file.write(history_text)

    print("Inventory saved successfully.")  

inventory, history = load_inventory()

print("Previous inventory:", inventory)
print("Previous transaction history:", history)

delivery_process = 0
failed_entries = 0

while True:
    stock = get_valid_input()

    if stock == 'quit':
        save_inventory(inventory, history)
        generate_report(inventory, failed_entries)
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery_(inventory, stock)

    history.append(stock)
    print("Transaction history:", history)

    tax = calculate_tax(inventory)

    delivery_process += 1

    print("Delivery amount:", stock)
    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)

print("Total deliveries processed:", delivery_process)
generate_report(inventory, failed_entries)


    