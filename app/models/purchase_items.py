class Purchase_Items:

    def __init__(self, item_name, count_of_item, item_unit_price):
        self.item_name = item_name
        self.count_of_item = count_of_item
        self.item_unit_price = item_unit_price

    def get_cost_of_items(self):
        return self.item_unit_price * self.count_of_item
