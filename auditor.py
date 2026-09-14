inventory = 0 
failed_entries = 0

while True:
    stock = input("Enter the stock item (or type 'quit' to exit): ")
    if stock.lower() == 'quit':
        print("Total inventory:", inventory)
        print("Failed entries:", failed_entries)
        break

    if stock.startswith("-") and stock[1:].isdigit():
        print("Invalid input. Please enter a positive value.")
        failed_entries += 1
        continue

    elif not stock.isdigit():
        print("Invalid input. Please enter a number.")
        failed_entries += 1
        continue
    else:
        stock = int(stock)
        inventory += stock

        if inventory > 500:
            print("Warning: Inventory is above 500 units.")
            break 

        


       
