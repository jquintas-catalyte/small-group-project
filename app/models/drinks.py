"""Drinks model definitions."""
class Drink:
    """
    A class representing a drink product.
    Attributes:
        name (str): The name of the drink product.
        ingredients (list[dict]): A list of ingredients for the drink.
        cost_to_produce (float): The cost to produce the drink.
        markup_percentage (float): The percentage to mark up the cost.
        sale_price (float): The total cost including markup.
    """
    def __init__(self, name: str, ingredients: list[dict], markup_percentage: float):
        """Initializes a Drink object.

        Args:
            name (str): The name of the drink.
            ingredients (list[dict]): A list of ingredients in the drink.
            cost_to_produce (float): The base cost to produce the drink.
            markup_percentage (float): The percentage to mark up the cost.
        """
        self.name = name
        self.ingredients = ingredients  # format list[{name: str, amount: float | int, price_per_unit: float}]
        self.markup_percentage = markup_percentage

    def __repr__(self):
        return f"Drink(name={self.name}, ingredients={self.ingredients}, sale_price={self.sale_price:.2f}, markup_percentage={self.markup_percentage}, cost_to_produce={self.cost_to_produce})"

    @property
    def cost_to_produce(self):
        """float: The total cost of ingredients markup."""
        return sum(ing['amount'] * ing['price_per_unit'] for ing in self.ingredients)

    @property
    def sale_price(self):
        """float: The total cost including markup."""
        return self.cost_to_produce * (1 + self.markup_percentage / 100)