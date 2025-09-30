""" Repository of Purchases """
import os
import pandas as pd 
from models import Purchase, PurchaseItem
from . import root_data_path
class PurchasesRepository:
    """ 
    Manages a collection of Purchase objects, acting as a data repository.
    This class handles operations such as creating new orders, retrieving existing 
    orders by ID, adding items to orders, and generating receipts. 
    """
    
    def __init__(self):
        """ 
        Initializes the repository with an existing list of Purchase objects.
        
        Parameters:
            data (list[Purchase]): The list where Purchase objects are stored.
        """
        self._df: pd.DataFrame

        self._data_filepath = os.path.join(root_data_path, "purchases_inventory.csv")
        if not os.path.exists(self._data_filepath):
            raise FileNotFoundError()
        
        self._df = pd.read_csv(self._data_filepath, index_col="purchase_id")
        self._save()

    def _save(self):
        self._df.to_csv(self._data_filepath)

    def create_purchase(self):
        """
        Creates a new empty purchase order and adds it to the system's data store.

        The new purchase is initialized with an 'unpaid' status and a unique ID.

        Returns:
            int: The unique identifier (purchase_id) of the newly created purchase.
        """
        purchase = Purchase()
        self._df.loc[len(self._df)] = {
            "purchase_id": purchase.purchase_id,
            "status": purchase.status,
            "date": purchase.purchase_date,
            "items": []
        }
        self._save()
        return purchase.purchase_id

    def get_purchase(self, purchase_id: int):
        """
        Retrieves a specific Purchase object from the data store by its ID.

        Parameters:
            purchase_id (int): The unique ID of the purchase to retrieve.

        Returns:
            Purchase: The matching Purchase object.

        Raises:
            KeyError: If no purchase with the given ID is found in the data store.
        """
        matching = self._df.loc[purchase_id]
        try: 
            purchase = Purchase(purchase_id=matching['purchase_id'], status=matching['status'], items=matching['items'], date=matching['date'])
            return purchase
            
        except KeyError as e:
            raise e
        
    def update_purchase(self, purchase: Purchase):
        pass


    def update_purchase_items(self, purchase_id: int, item):
        """
        Adds a single item (Purchase_Item) to an existing purchase order.

        It first retrieves the purchase using the ID and then calls the 
        purchase's internal add_item method.

        Parameters:
            purchase_id (int): The unique ID of the purchase to update.
            item: The item object (expected to have a 'total_price' attribute) to be added.
        
        Raises:
            KeyError: If no purchase with the given ID is found (inherited from get_purchase).
        """
        purchase = self.get_purchase(purchase_id)
        purchase.add_item(item)
        self.update_purchase(purchase)
        

    def shop_receipt(self, purchase_id: int):
        """
        Generates a list representing a receipt for a specific purchase.
        It retrieves the full purchase details using the given ID and compiles 
        the relevant information (date, items, and total cost).

        Parameters:
            purchase_id (int): The unique ID of the purchase order.

        Returns:
            list[str]: A list of strings, where each string is a line on the receipt.

        Raises:
            KeyError: If the purchase_id is not found (inherited from get_purchase).
        """
        
        purchase = self.get_purchase(purchase_id) 
        receipt = []
        receipt.append("--- Express O Coffee ---")
        receipt.append(f"Date: {purchase.purchase_date}")
        receipt.append(f"Receipt Number: {purchase.purchase_id}")
        receipt.append("-" * 30)

        if purchase.items:
            for item in purchase.items:
                item_cost = item.get_purchase_cost_of_items() 
                receipt.append(f"  {item.item_name:<20} ${item_cost:5.2f}") 
        else:
            receipt.append("  -- No items purchased --")

        receipt.append("-" * 30)
        
        final_total = purchase.total_cost()
        receipt.append(f"Total Cost: {' ' * 14} ${final_total:5.2f}") 
        receipt.append("--------------------------")
        
        return receipt

