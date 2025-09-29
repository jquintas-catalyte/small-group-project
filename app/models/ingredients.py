class Ingredients:
    def __init__(
        self, item_name, purchasing_cost, unit_amount, unit_of_measure, inventory
    ):
        self.item_name = item_name
        self.purchasing_cost = purchasing_cost
        self.unit_amount = unit_amount
        self.unit_of_measure = unit_of_measure
        self.inventory = inventory
