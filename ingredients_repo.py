from app.models import ingredients


class IngredientRepository:

    def get_ingredients(self):
        return {
            "item name": self.item_name,
            "category": self.category,
        }

    def update_count(inventory, item_name, amount):

        if item_name in inventory and inventory[item_name] >= amount:
            inventory[item_name] -= amount
            print(
                f"Decremented {amount} {item_name}(s). New quantity: {inventory[item_name]}"
            )
        elif item_name not in inventory:
            print(f"Error: {item_name} not found in inventory.")
        else:
            print(f"Error: Insufficient quantity of {item_name}.")

    class IngredientRepository:
    """
    A repository for managing Ingredient objects.
    """

    def __init__(self):
        # in-memory storage for now
        self._ingredients = {}

    def add(self, ingredient):
        self._ingredients[ingredient.item_name] = ingredient

    def get(self, item_name):
        return self._ingredients.get(item_name)

    def list_all(self):
        return list(self._ingredients.values())

    def update(self, item_name, **kwargs):
        ingredient = self._ingredients.get(item_name)
        if ingredient:
            for key, value in kwargs.items():
                setattr(ingredient, key, value)
            return ingredient
        return None

    def delete(self, item_name):
        return self._ingredients.pop(item_name, None)

    def use(self, item_name: str, amount: float):
        """
        Decrement the inventory of an ingredient when it is used.

        Parameters
        ----------
        item_name : str
            The name of the ingredient to decrement.
        amount : float
            How much of the ingredient is being used.

        Returns
        -------
        Ingredient | None
            The updated ingredient object if found, otherwise None.

        Raises
        ------
        ValueError
            If amount exceeds the available inventory.
        """
        ingredient = self._ingredients.get(item_name)
        if not ingredient:
            return None

        if ingredient.inventory < amount:
            raise ValueError(
                f"Not enough {ingredient.item_name} in stock. "
                f"Available: {ingredient.inventory}, requested: {amount}"
            )

        ingredient.inventory -= amount
        return ingredient

    def calculate_cost(self, item_name: str, requested_amount: float, unit_of_measure: str) -> float:
            """
        Calculate the purchasing cost for a requested amount of an ingredient.

        Parameters:
            item_name (str): The name of the ingredient.
            requested_amount (float): The amount needed.
            unit_of_measure (str): The unit of measurement of the requested amount.

        Returns:
            float: The cost for the requested amount.

        Raises:
            ValueError: If the ingredient is not found or units don’t match.
        """
            if item_name not in self.ingredients:
                raise ValueError(f"Ingredient '{item_name}' not found in repository.")

            ingredient = self.ingredients[item_name]

            if unit_of_measure != ingredient.unit_of_measure:
                raise ValueError(
                f"Unit mismatch: {unit_of_measure} vs {ingredient.unit_of_measure}"
            )

        # Unit price = cost / amount purchased
            unit_price = ingredient.purchasing_cost / ingredient.unit_amount

            return round(unit_price * requested_amount, 2)
