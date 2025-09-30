from ..models.purchase import Purchase, Purchase_Item

class PurchasesRepository:
    """ A repository of purchases """
    
    def __init__(self, data: list[Purchase]):
        """ Initalize  the repository
        Expection: No ID Found
        """
        self.data:list[Purchase] = data

    def create_purchase(self):
        """
        Creates a new empty purchase order and adds it to the system's data store.

        The new purchase is initialized with an 'unpaid' status and a unique ID.

        Returns:
            int: The unique identifier (purchase_id) of the newly created purchase.
        """
        purchase = Purchase()
        self.data.append(purchase)
        return purchase.purchase_id

    def get_purchase(self, purchase_id: int):
        """
        Retrieves a specific Purchase object from the data store by its ID.

        Parameters:
            purchase_id (int): The unique ID of the purchase to retrieve.

        Returns:
            Purchase: The matching Purchase object.

        Raises:
            Exception: If no purchase with the given ID is found in the data store.
        """
        matching = [purchase for purchase in self.data if purchase.purchase_id == purchase_id]
        if len(matching):
            return matching[0]
        else:
            raise Exception("No ID Found")

    def update_purchase_items(self, purchase_id: int, item):
        """
        Adds a single item (Purchase_Item) to an existing purchase order.

        It first retrieves the purchase using the ID and then calls the 
        purchase's internal add_item method.

        Parameters:
            purchase_id (int): The unique ID of the purchase to update.
            item: The item object (expected to have a 'total_price' attribute) to be added.
        
        Raises:
            Exception: If no purchase with the given ID is found (inherited from get_purchase).
        """
        purchase = self.get_purchase(purchase_id)
        purchase.add_item(item)

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
            ValueError: If the purchase_id is not found (inherited from get_purchase).
        """
        
        purchase = self.get_purchase(purchase_id) 
        receipt = []
        receipt.append("--- Express O Coffee ---")
        receipt.append(f"Date: {purchase.purchase_date}")
        receipt.append(f"Receipt Number: {purchase.purchase_id}")
        receipt.append("-" * 30)

        if purchase.items:
            for item in purchase.items:
                receipt.append(f"  {item.name:<20} ${item.total_price:5.2f}") 
        else:
            receipt.append("  -- No items purchased --")

        receipt.append("-" * 30)
    
        final_total = purchase.total_cost()
        receipt.append(f"Total Cost: {' ' * 14} ${final_total:5.2f}") 
        receipt.append("--------------------------")
    
        return receipt

