from app.repositories.ingredients_repo import IngredientsRepo
from ingredients import Ingredient


class IngredientService:
    """
    Service layer for managing ingredients through the repository.
    """

    def __init__(self, repo: IngredientsRepo):
        self.repo = repo

    def add_new_ingredient(
        self,
        item_name: str,
        category: str,
        purchasing_cost: float,
        unit_amount: float,
        unit_of_measure: str,
        inventory: float,
    ):
        """
        Create and add a new ingredient to the repository.
        """
        ingredient = Ingredient(
            item_name=item_name,
            category=category,
            purchasing_cost=purchasing_cost,
            unit_amount=unit_amount,
            unit_of_measure=unit_of_measure,
            inventory=inventory,
        )
        self.repo.add_ingredient(ingredient)

    def calculate_cost_for_amount(
        self, item_name: str, requested_amount: float, unit_of_measure: str
    ) -> float:
        """
        Calculate the cost for a given amount of an ingredient.
        """
        return self.repo.calculate_cost(item_name, requested_amount, unit_of_measure)

    def use_ingredient(
        self, item_name: str, requested_amount: float, unit_of_measure: str
    ) -> float:
        """
        Deducts inventory when using an ingredient and returns its cost.
        """
        ingredient = self.repo.ingredients.get(item_name)
        if not ingredient:
            raise ValueError(f"Ingredient '{item_name}' not found.")
        if ingredient.unit_of_measure != unit_of_measure:
            raise ValueError("Unit mismatch.")
        if requested_amount > ingredient.inventory:
            raise ValueError(f"Not enough {item_name} in inventory.")

        ingredient.inventory -= requested_amount
        return self.repo.calculate_cost(item_name, requested_amount, unit_of_measure)

    def restock_ingredient(self, item_name: str, amount: float):
        """
        Add stock back into an ingredient's inventory.
        """
        ingredient = self.repo.ingredients.get(item_name)
        if not ingredient:
            raise ValueError(f"Ingredient '{item_name}' not found.")

        ingredient.inventory += amount
