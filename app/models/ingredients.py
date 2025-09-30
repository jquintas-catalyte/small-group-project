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
        item_name,
        category,
        purchasing_cost,
        unit_amount,
        unit_of_measure,
        inventory,
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
        self.inventory = inventory
