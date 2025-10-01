from repositories import IngredientRepository
from models import Ingredient


class IngredientService:
    """
    Service layer for managing ingredients via the IngredientRepository.
    Handles higher-level business logic such as using ingredients,
    restocking, and calculating costs.
    """

    def __init__(self, repository: IngredientRepository):
        """
        Initialize the service with an IngredientRepository.
        """
        self._repository = repository

    def get_ingredient_by_name(self, item_name: str) -> Ingredient:
        """
        Retrieve an ingredient by name.

        Parameters:
            item_name (str): The name of the ingredient to retrieve.

        Returns:
            Ingredient: The requested ingredient.

        Raises:
            ItemNotFound: If the ingredient is not found in the repository.
        """
        return self._repository.get_item_by_name(item_name)

    def get_items_by_name(self, item_names: list[str]) -> list[Ingredient]:
        """
        Retrieve a list of ingredients by their names.

        Parameters:
            item_name (str): The name of the ingredient to retrieve.

        Returns:
            list[Ingredient]: List of the requested ingredients.

        Raises:
            ItemNotFound: If any ingredient is not found in the repository.
        """
        return self._repository.get_items_by_name(item_names)

    def is_in_stock(self, item_name: str, amount_needed: float | None = None) -> bool:
        """
        Check if an ingredient is in stock.

        Parameters:
            item_name (str): The name of the ingredient to check.
            amount_needed (float): The amount needed to check against inventory.
        Returns:
            bool: True if the ingredient is in stock, False otherwise.
        """
        return self._repository.is_item_in_stock(item_name, amount_needed)

    def get_items_by_category(self, category: str) -> list[Ingredient]:
        """
        Retrieve all ingredients in a given category.

        Parameters:
            category (str): The category to filter ingredients by.
        Returns:
            list[Ingredient]: List of ingredients in the specified category.
        """
        return self._repository.get_items_by_category(category)

    def get_all(self):
        return self._repository.get_all()