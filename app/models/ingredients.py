class Ingredient:
     '''represents an ingredient with purchasing details
     item_name (str): The name of the ingredient (e.g., "Flour").
        purchasing_cost (float): The cost of purchasing the ingredient 
            per unit_amount in the given unit_of_measure.
        unit_amount (float): The quantity that the purchasing cost corresponds to.
        unit_of_measure (str): The unit of measurement for the ingredient 
            (e.g., "kg", "liter", "pack")'''.

     def __init__(
        self, item_name, purchasing_cost, unit_amount, unit_of_measure, inventory
    ):
        self.item_name = item_name
        self.purchasing_cost = purchasing_cost
        self.unit_amount = unit_amount
        self.unit_of_measure = unit_of_measure
        self.inventory = inventory

        

        
