"""Definitions for Ingredient class"""


class Ingredient:
    """
    Represents an ingredient.
    Attributes:
        item_name (str): The name of the ingredient (e.g., "Flour").
        purchasing_cost (float): The cost of purchasing the ingredient per unit_amount.
        unit_amount (float): The quantity that the purchasing cost corresponds to.
        unit_of_measure (str): The unit of measurement for the ingredient.
        category (str): The product category.
    """

    def __init__(
        self,
        item_name: str,
        category: str,
        purchasing_cost: float,
        unit_amount: float,
        unit_of_measure: str,
    ):
        """
        Initializes the Ingredient class.

        Parameters:
            item_name (str): The name of the ingredient (e.g., "Flour").
            category (str): The product category.
            purchasing_cost (float): The cost of purchasing the ingredient per unit_amount.
            unit_amount (float): The quantity of the product in the inventory.
            unit_of_measure (str): The unit of measurement for the ingredient.
        """

        self.item_name = item_name
        self.category = category
        self.purchasing_cost = purchasing_cost
        self.unit_amount = unit_amount
        self.unit_of_measure = unit_of_measure
    def __repr__(self):
        return f"Ingredient(item_name={self.item_name}, category={self.category}, purchasing_cost={self.purchasing_cost}, unit_amount={self.unit_amount}, unit_of_measure={self.unit_of_measure})"
    
    @property
    def cost_per_unit(self) -> float:
        """
        Calculate the cost per unit of the ingredient.
        Returns:
            float: The cost per unit.
        """
        return self.purchasing_cost / self.unit_amount
    
    def is_in_stock(self) -> bool:
        """
        Check if the ingredient is in stock.
        Returns:
            bool: True if in stock, False otherwise.
        """
        return self.unit_amount > 0
    
    def can_use(self, amount_needed: float) -> bool:
        """
        Check if the requested amount of the ingredient can be used.
        Parameters:
            amount (float): The amount to check.
        Returns:
            bool: True if the amount can be used, False otherwise.
        """
        return self.unit_amount >= amount_needed