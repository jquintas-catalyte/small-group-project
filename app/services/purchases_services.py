""" Definition of Purchase Services """
from repositories import PurchasesRepository
from models import PurchaseItem

class PurchaseServices:
    """
    Handles the business logic for all purchase-related operations.

    This class serves as an intermediary between the application's user interface 
    and the PurchasesRepository, ensuring data integrity and executing complex tasks.
    """
    def __init__ (self, repository: PurchasesRepository) -> None:
        """ 
        Initializes the PurchaseServices with a dependency on the data repository.
        """
        self.purchases_repository = repository
    
    def create_new_order(self):
        """
        Initiates a new purchase order in the system.

        Returns:
            int: The ID of the newly created order.
        """
        return self.purchases_repository.create_purchase()
    
    def add_item_to_order(self, purchase_id: int, item:PurchaseItem):
        """
        Adds a single item to existing, active purchase order.

        Parameters:
            purchase_id (int): The ID of the order to update.
            item (PurchaseItem): The item added to the order.

        Raises: 
            KeyError: If purchase ID isn't found
        """
        self.purchases_repository.update_purchase_items(purchase_id, item)

    def generate_receipt(self, purchase_id: int):
        """
        Generates a formatted list of strings representing the final receipt 
        for a completed order.

        Parameters:
            purchase_id (int): The ID of the order for which to generate the receipt.

        Returns:
            list[str]: A list of strings, ready to be printed or displayed.

        Raises:
            KeyError: If the purchase ID is not found.
        """
        return self.purchases_repository.shop_receipt(purchase_id)

