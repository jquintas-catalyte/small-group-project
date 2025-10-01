"""Baked Goods Service Layer"""
from repositories import BakedGoodsRepository
from models import BakedGood
from exceptions import ItemNotFound


class BakedGoodsService:
    """Service layer for baked goods."""

    def __init__(self, repository: BakedGoodsRepository | None = None):
        """
        Initializes the baked goods service with an optional repository instance.

        Args:
            repository (BakedGoodsRepository, optional): The repository to use.
        """
        self._repository = repository or BakedGoodsRepository()

    def get_product(self, name: str) -> BakedGood:
        """
        Gets a single baked good by name.

        Args:
            name (str): The name of the baked good.

        Returns:
            BakedGood: The matching baked good.

        Raises:
            ItemNotFound: If no baked good matches the name.
        """
        return self._repository.get_product_by_name(name)

    def list_products(self) -> list[BakedGood]:
        """
        Lists all baked goods.

        Returns:
            list[BakedGood]: All baked goods.
        """
        return self._repository.list_all_products()

    def get_low_stock_items(self, threshold: int = 5) -> list[BakedGood]:
        """
        Returns baked goods with stock count below a given threshold.

        Args:
            threshold (int): The stock count threshold.

        Returns:
            list[BakedGood]: List of low stock items.
        """
        return [product for product in self.list_products() if product.count < threshold]