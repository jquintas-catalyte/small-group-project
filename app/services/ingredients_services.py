from repositories import IngredientRepository
from models import Ingredient


class IngredientService:
    """
    Service layer for managing ingredients via the IngredientRepository.
    Handles higher-level business logic such as using ingredients,
    restocking, and calculating costs.
    """

    def __init__(self, repo: IngredientRepository):
        """
        Initialize the service with an IngredientRepository.
        """
        self.repo = repo

    def calculate_cost_for_amount(
        self, item_name: str, requested_amount: float
    ) -> float:
        """
        Calculate the purchasing cost for a given amount of an ingredient.

        Args:
            item_name (str): Name of the ingredient.
            requested_amount (float): The amount of the ingredient needed.

        Returns:
            float: Cost for the requested amount.

        Raises:
            ItemNotFound: If the ingredient does not exist.
        """
        ingredient = self.repo.get_item(item_name)

        # Unit price = purchasing_cost / unit_amount
        unit_price = ingredient.purchasing_cost / ingredient.unit_amount
        return round(unit_price * requested_amount, 2)

    def use_ingredient(self, item_name: str, requested_amount: float) -> float:
        """
        Deduct an ingredient from inventory and return its cost.

        Args:
            item_name (str): Ingredient name.
            requested_amount (float): Amount to use.

        Returns:
            float: The cost of the requested amount.

        Raises:
            ValueError: If not enough inventory is available.
            ItemNotFound: If ingredient is not found.
        """
        if not self.repo.is_item_in_stock(item_name, requested_amount):
            raise ValueError(
                f"Not enough {item_name} in stock to use {requested_amount} units."
            )

        # Update inventory (deduct)
        self.repo.update_inventory(item_name, -requested_amount)

        # Calculate cost
        return self.calculate_cost_for_amount(item_name, requested_amount)

    def restock_ingredient(self, item_name: str, units: float):
        """
        Add stock for an ingredient.

        Args:
            item_name (str): Ingredient name.
            units (float): Number of units to add.

        Raises:
            ItemNotFound: If the ingredient does not exist.
        """
        self.repo.update_inventory(item_name, units)

    def get_ingredient_info(self, item_name: str) -> dict:
        """
        Retrieve structured information about an ingredient.

        Args:
            item_name (str): Ingredient name.

        Returns:
            dict: Ingredient details (name, category, cost, inventory, etc.).
        """
        ingredient = self.repo.get_item(item_name)
        return {
            "item_name": ingredient.item_name,
            "category": ingredient.category,
            "unit_amount": ingredient.unit_amount,
            "unit_of_measure": ingredient.unit_of_measure,
            "purchasing_cost": ingredient.purchasing_cost,
            "inventory": ingredient.inventory,
        }
