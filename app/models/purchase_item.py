class Purchase_Item:

    def __init__(self, item_name, count_of_item, item_unit_price):
        self.item_name = item_name
        self.count_of_item = count_of_item
        self.item_unit_price = item_unit_price

    def get_cost_of_items(self):
        return self.item_unit_price * self.count_of_item

    def __str__(self):
        purchase_cost = self.get_cost_of_items()
        return f"Name: {self.item_name} Count: {self.count_of_item} Unit Price: ${self.item_unit_price:.2f} Purchase Cost ${purchase_cost:.2f}"


item_1 = Purchase_Item("Coffee", 2, 1.25)
print(item_1)
