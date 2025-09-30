from models.drinks import Drink
from repositories.drinks_repository import DrinkRepository

class DrinkService:
    def __init__(self, drink_repository: DrinkRepository):
        """Initializes the service with a repository instance."""
        self._drink_repository = drink_repository

    def create_drink(self, drink_data: dict) -> Drink:
        

