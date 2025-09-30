from models.drinks import Drink
class DrinkRepository:
    def __init__(self):
        self._drinks = {}

    def add(self, drink: Drink):
        """Adds new drink to repository"""
        if not isinstance(drink, Drink):
            raise TypeError("Only Drink objects can be added to repository.")
        if drink.name in self._drinks:
            raise ValueError(f"Drink with name {drink.name} already exists")
        self._drinks[drink.name] =drink
        print(f"Added drink: {drink.name}")

    def get(self, name: str):
        """Retrieves a drink by name."""
        return self._drinks.get(name)
    
    def get_all(self):
        """Returns a list of all drinks in repository."""
        return list(self._drinks.values())
    
    def update(self, drink: Drink):
        """Updates an existing drink in the repository."""
        if drink.name not in self.drinks:
            raise ValueError(f"Drink with name {drink.name} not found.")
        self._drinks[drink.name] = drink
        print(f"Updated drink: {drink.name}")

    def delete(self, name: str):
        """Deletes a drink from within the repository by name"""
        if name not in  self._drinks:
            raise ValueError(f"Drink with name {name} not found.")
        del self._drinks[name]
        print(f"Deleted drink: {name}")


if __name__ == "__main__":
    """Creates repository."""
    repo = DrinkRepository()

    """Defines some ingredients"""






    """Creates new Drink objects"""