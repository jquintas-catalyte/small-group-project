import ast
import os
import pandas as pd
from models import BakedGood
from . import root_data_path

class BakedGoodsRepository:
    def __init__(self):
        self._df: pd.DataFrame
        self._data_filepath = os.path.join(root_data_path, "baked_goods_inventory.csv")
        if os.path.exists(self._data_filepath):
            self._df = pd.read_csv(self._data_filepath, converters={"known_allergens": ast.literal_eval})
        else:
            self._df = pd.DataFrame(columns=["name", "vendor_name", "purchasing_cost", "markup_percentage", "known_allergens", "count"])
            self.save()

    def save(self):
        """
        Save the changes to the inventory.
        Raises:
            FileNotFoundError: If data file is not found.
        """
        if not os.path.exists(self._data_filepath):
            raise FileNotFoundError(f"The file {self._data_filepath} was not found.")
        self._df.to_csv(self._data_filepath, index=False)

    def add_product(self, product: BakedGood):
        """
        Adds a new pruduct to the inventory.
        Args:
            product (BakedGood): The product to add.
        """
        if product.name in self._df["name"].values:
            raise ValueError(f"Baked good with name '{product.name}' already exists.")
        new_row = {
            "name": product.name,
            "vendor_name": product.vendor_name,
            "purchasing_cost": product.purchasing_cost,
            "markup_percentage": product.markup_percentage,
            "known_allergens": product.known_allergens,
            "count": product.count,
        }
        self._df = self._df.append(new_row, ignore_index=True)
        self.save()

    def get(self, name: str) -> BakedGood | None:
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

    def update(self, name: str, updates: dict):
        index = self._df[self._df["name"] == name].index
        if index.empty:
            raise ValueError(f"Baked good with name '{name}' not found.")
        for key, value in updates.items():
            if key not in self._df.columns:
                raise KeyError(f"Invalid field: {key}")
            self._df.at[index[0], key] = value
        self.save()

    def list_all(self) -> list[BakedGood]:
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



