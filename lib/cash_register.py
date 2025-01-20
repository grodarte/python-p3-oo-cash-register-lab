#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0, total = 0):
        self.discount = discount
        self.total = total
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity = 1):
        self.total += (price * quantity)
        self.items.extend([title for number in range(quantity)])
        self.last_transaction = price * quantity


    def apply_discount(self):
        if self.discount:
            self.total -= self.discount / 100 * self.total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def items(self):
        return self.items
    
    def void_last_transaction(self):
        self.total -= self.last_transaction