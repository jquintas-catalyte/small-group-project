"""Ingredient repository module."""

import os, pandas as pd
from models import Ingredient
from repositories import root_data_path
from exceptions import ItemNotFound


class IngredientRepository:
    """Repository for managing Ingredient objects."""

    def __init__(self):
        """Initializes the repository.

        Raises:
            FileNotFoundError: If data file path is invalid.
        """
        self._df: pd.DataFrame
        self._data_filepath = os.path.join(root_data_path, "ingredients_inventory.csv")
        if not os.path.exists(self._data_filepath):
            raise FileNotFoundError(f"The file {self._data_filepath} was not found.")
        self._df = pd.read_csv(self._data_filepath)

    def _save(self):
        """
        Save the changes to the inventory.
        Raises:
            FileNotFoundError: If data file is not found.
        """
        if not os.path.exists(self._data_filepath):
            raise FileNotFoundError(f"The file {self._data_filepath} was not found.")
        self._df.to_csv(self._data_filepath, index=False)

    def _get_item_row(self, item_name: str) -> pd.Series:
        item = self._df[self._df["name"] == item_name]
        if item.empty:
            raise ItemNotFound(f"Ingredient '{item_name}' not found.")
        return item.iloc[0]

    def get_item(self, item_name: str) -> Ingredient:
        """
        Get an ingredient by name.
        Args:
            item_name (str): The name of the ingredient.
        Returns:
            Ingredient: The ingredient object.
        Raises:
            ItemNotFound: If the ingredient is not found.
            ValueError: If expected columns are missing in the data.
        """
        item = self._get_item_row(item_name)
        try:
            return Ingredient(
                item_name=item["name"],
                category=item["category"],
                purchasing_cost=item["purchasing_cost"],
                unit_amount=item["unit_amount"],
                unit_of_measure=item["unit_of_measure"],
                inventory=item["inventory"],
            )
        except KeyError as e:
            raise ValueError(f"Missing expected column in data: {e}")

    def get_items(self, item_names: list[str]) -> list[Ingredient]:
        """
        Get multiple ingredients by their names.
        Args:
            item_names (list[str]): List of ingredient names.
        Returns: list[Ingredient]: List of ingredient objects.
        Raises:
            ItemNotFound: If any ingredient is not found.
        """
        return [self.get_item(name) for name in item_names]

    def is_item_in_stock( self, item_name: str, amount_needed: float | None = None ) -> bool:
        item = self.get_item(item_name)
        return item.is_in_stock() if not amount_needed else item.can_use(amount_needed)

    def update_inventory(self, item_name: str, units: float):
        item = self._get_item_row(item_name)
        itemp = item.to_dict()
        if itemp["unit_amount"] + units < 0:
            raise ValueError(f"Not enough {item_name} in inventory to deduct {units}.")
        itemp["unit_amount"] += units
        self._df.loc[self._df["item_name"] == item_name, "unit_amount"] = itemp[
            "unit_amount"
        ]
        self._save()
