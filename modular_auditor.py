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

delivery_process = 0
inventory = 0 
failed_entries = 0

while True:
    stock = get_valid_input()

    if stock == 'quit':
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery_(inventory, stock)

    tax = calculate_tax(inventory)

    delivery_process += 1

    print("Delivery amount:", stock)
    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)

    print("Total deliveries processed:", delivery_process)
    generate_report(inventory, failed_entries)


    