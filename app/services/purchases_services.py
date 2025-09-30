""" Definition of Purchase Services """
from ..repositories import purchases_repository
from ..models.purchase import PurchaseItem

class PurchaseServices:
    """
    Handles the business logic for all purchase-related operations.

    This class serves as an intermediary between the application's user interface 
    and the PurchasesRepository, ensuring data integrity and executing complex tasks.
    """
    def __init__ (self, repository: purchases_repository) -> None:
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
    
    
