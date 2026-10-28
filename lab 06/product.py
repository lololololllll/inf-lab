class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        if quantity >= 0:
            self.__stock = quantity
            print("Stock updated successfully.")
        else:
            print("Stock cannot be negative.")

    def display_information(self):
        print("Product ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $", self.__price)
        print("Stock:", self.__stock)
        print("--------------------")

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
