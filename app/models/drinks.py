class Drink:
    def __init__(self, name, ingredients, cost_to_produce, markup_percentage):
        """Initializes a Drink object.

        Args:
            name (str): The name of the drink.
            ingredients (list): A list of ingredients in the drink.
            cost_to_produce (float): The base cost to produce the drink.
            markup_percentage (float): The percentage to mark up the cost.
        """
       
        self.name = name
        self.ingredients = ingredients
        self.cost_to_produce = cost_to_produce
        self.markup_percentage = markup_percentage
        self.sale_price = cost_to_produce * (1 + markup_percentage / 100)

    def __repr__(self):
        return f"Drink(name={self.name}, ingredients={self.ingredients}, sale_price={self.sale_price:.2f}, markup_percentage={self.markup_percentage}, cost_to_produce={self.cost_to_produce} )"






    



