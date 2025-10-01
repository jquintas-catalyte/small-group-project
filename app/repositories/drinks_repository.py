import ast
import os
import pandas as pd
from models import Drink
from . import root_data_path
from exceptions import ItemNotFound

class DrinkRepository:
    def __init__(self):
        """
        Initializes the repository.
        Raises:
            FileNotFoundError: If data file path is invalid.
        """
        self._df: pd.DataFrame
        self._data_filepath = os.path.join(root_data_path, "drinks_inventory.csv")
        if not os.path.exists(self._data_filepath):
            raise FileNotFoundError(f"The file {self._data_filepath} was not found.")
        self._df = pd.read_csv(self._data_filepath)

    def get_drink_by_name(self, drink_name:str):
        """
        Gets a drink by name.
        Args:
            drink_name (str): The name of the drink to get.
        Raises:
            ItemNotFound: If drink does not exist
            KeyError: If row does not have needed Drink  constructor args.

        Returns:
            Drink: Drink matching provided name.
        """
        row = self._df[self._df["name"] == drink_name]
        if row.empty:
            raise ItemNotFound(f"Drink with name '{drink_name}' was not found")
        row = row.iloc[0]
        try:
            return Drink(
                name=row["name"],
                markup_percentage=row["markup_percentage"],
                ingredients=row["ingredients"],
            )
        except KeyError as e:
            raise e
        
    def get_all(self):
        """
        Returns a list of all drinks in repository.
        Returns:
            list[Drink]: The list of all drinks.
        """
        drinks: list[Drink] = []
        for _, item in self._df.iterrows():
            drinks.append(
                Drink(
                    name=item['name'],
                    ingredients=item['ingredients'],
                    markup_percentage=item['markup_percentage']
                )
            )    
        return drinks



