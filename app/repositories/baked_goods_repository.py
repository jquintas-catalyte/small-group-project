"""Baked goods repository module."""
import ast
import os
import pandas as pd
from models import BakedGood
from . import root_data_path
from exceptions import ItemNotFound


class BakedGoodsRepository:
    """Baked Goods Repository."""
    def __init__(self):
        """
        Initializes the repository.
        Raises:
            FileNotFoundError: If data file path is invalid.
        """
        self._df: pd.DataFrame
        self._data_filepath = os.path.join(root_data_path, "baked_goods_inventory.csv")
        if not os.path.exists(self._data_filepath):
            raise FileNotFoundError(f"The file {self._data_filepath} was not found.")
        self._df = pd.read_csv(self._data_filepath, converters={"known_allergens": ast.literal_eval})

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
        """
        Gets the item row in the database.

        Args:
            item_name (str): The item to lookup.

        Raises:
            ItemNotFound: If matching row does not exist.

        Returns:
            pd.Series: The matching row
        """
        item = self._df[self._df["name"] == item_name]
        if item.empty:
            raise ItemNotFound(f"Ingredient '{item_name}' not found.")
        return item.iloc[0]

    def get_product_by_name(self, product_name: str) -> BakedGood:
        """Get a product by name
        Args:
            name (str): The product name
        Returns:
            BakedGood | None: The product if found 
        """
        product = self._get_item_row(product_name)
        try:
            return BakedGood(
                name=product["name"],
                vendor_name=product["vendor_name"],
                purchasing_cost=product["purchasing_cost"],
                markup_percentage=product["markup_percentage"],
                known_allergens=product["known_allergens"],
                count=product["count"],
            )
        except KeyError as e:
            raise e

    def list_all_products(self) -> list[BakedGood]:
        """
        Lists all baked goods.
        Returns:
            list[BakedGood]: The list of baked goods.
        """
        goods: list[BakedGood] = []
        for _, row in self._df.iterrows():
            goods.append(
                BakedGood(
                    name=row["name"],
                    vendor_name=row["vendor_name"],
                    purchasing_cost=row["purchasing_cost"],
                    markup_percentage=row["markup_percentage"],
                    known_allergens=row["known_allergens"],
                    count=row["count"],
                )
            )
        return goods
