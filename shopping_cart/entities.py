class Product():

    def __init__(self, description: str, price: float):
        self.description = description
        self.price = price

    def __str__(self):
        return f"[{self.description} - {self.price}]"

class Item():

    def __init__(self, amount, product):
        self.amount = amount
        # relación de composición
        self.product = product

    def get_subtotal(self):
        return self.product.price * self.amount
    
    def __str__(self):
        return f"Product: {self.product} - Amount: {self.amount} - Subtotal: {self.get_subtotal()}"
    
class Shop():

    def __init__(self, date, items=[]):
        self.date = date
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        return sum([ item.get_subtotal() for item in self.items ])