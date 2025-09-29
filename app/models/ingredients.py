class Ingredients:
    def __init__(
        self, item_name, purchasing_cost, unit_amount, unit_of_measure, inventory
    ):
        self.item_name = item_name
        self.purchasing_cost = purchasing_cost
        self.unit_amount = unit_amount
        self.unit_of_measure = unit_of_measure
        self.inventory = inventory

    def update_count(self, amount_used):
        if self.unit_amount >= amount_used:
            self.unit_amount -= amount_used
            return(
                f"Decremented {amount_used} of {self.item_name}. Remaining: {self.unit_amount}"
            )
        else:
            return(
                f"Not enough {self.item_name} available. Only {self.unit_amount} remaining."
            )

    def cost_for_purchase(self):
