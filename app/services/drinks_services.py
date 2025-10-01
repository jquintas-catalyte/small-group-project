from models import Drink
from repositories import DrinkRepository
from exceptions import ItemNotFound


class DrinkService:
    """
    Service layer for handling drink-related business logic and validations.
    This layer interacts with the DrinkRepository but never directly with the CSV.
    """

    def __init__(self, repository: DrinkRepository):
        self.repository = repository

    def validate_drink(self, drink: Drink) -> bool:
        """
        Validates a Drink object according to business rules.

        Args:
            drink (Drink): The drink to validate.

        Returns:
            bool: True if valid.

        Raises:
            ValueError: If validation fails.
        """
        if not drink.name or not isinstance(drink.name, str):
            raise ValueError("Drink name must be a non-empty string.")

        if not drink.ingredients or not isinstance(drink.ingredients, list):
            raise ValueError("Ingredients must be a non-empty list of dictionaries.")

        for ing in drink.ingredients:
            if not all(key in ing for key in ["name", "amount", "price_per_unit"]):
                raise ValueError(f"Ingredient missing required fields: {ing}")
            if ing["amount"] <= 0 or ing["price_per_unit"] <= 0:
                raise ValueError(f"Ingredient amounts and price must be positive: {ing}")

        if drink.markup_percentage < 0:
            raise ValueError("Markup percentage must be non-negative.")

        return True

    def create_drink(self, name: str, ingredients: list[dict], markup_percentage: float) -> Drink:
        """
        Creates a new Drink object after validation.
        This does not persist to repository.

        Args:
            name (str): Name of the drink.
            ingredients (list[dict]): Ingredients with keys 'name', 'amount', 'price_per_unit'.
            markup_percentage (float): Markup percentage.

        Returns:
            Drink: The validated drink object.
        """
        new_drink = Drink(
            name=name,
            ingredients=ingredients,
            markup_percentage=markup_percentage,
        )

        # Run validation before returning
        self.validate_drink(new_drink)

        return new_drink

    def get_drink(self, name: str) -> Drink:
        """
        Retrieves a drink by name via repository.

        Args:
            name (str): The drink name.

        Returns:
            Drink: Drink object.

        Raises:
            ItemNotFound: If the drink does not exist.
        """
        return self.repository.get_drink_by_name(name)

    def list_drinks(self) -> list[Drink]:
        """
        Returns all drinks via repository.

        Returns:
            list[Drink]: All drinks.
        """
        return self.repository.get_all()

    def calculate_sale_price(self, name: str) -> float:
        """
        Calculates sale price for an existing drink.

        Args:
            name (str): Drink name.

        Returns:
            float: Sale price.

        Raises:
            ItemNotFound: If drink not found.
        """
        drink = self.get_drink(name)
        return drink.sale_price
