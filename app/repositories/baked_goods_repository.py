"""Baked goods repository module."""
import ast
import os
import pandas as pd
from models import BakedGood
from . import root_data_path


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

    def get_product_by_name(self, name: str) -> BakedGood | None:
        """Get a product by name
        Args:
            name (str): The product name
        Returns:
            BakedGood | None: The product if found. 
        """
        row = self._df[self._df["name"] == name]
        if row.empty:
            return None
        row = row.iloc[0]
        return BakedGood(
            name=row["name"],
            vendor_name=row["vendor_name"],
            purchasing_cost=row["purchasing_cost"],
            markup_percentage=row["markup_percentage"],
            known_allergens=row["known_allergens"],
            count=row["count"],
        )

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
