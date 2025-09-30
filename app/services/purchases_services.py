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
            purchase_id (int): the ID of the order to update.
            item (PurchaseItem): the item added to the order.

        Raises: 
            KeyError: if purchase ID isn't found
        """
        self.purchases_repository.update_purchase_items(purchase_id, item)

        