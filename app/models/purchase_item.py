class PurchaseItem:

    def __init__(self, item_name, count_of_item, item_unit_price):
        """
        Initializes the PurchaseItem class
        Parameters:
            item_name (str): name of the item
            count_of_item (int): number of items
            item_unit_price (float): individual pricing for the item
        """
        self.item_name = item_name
        self.count_of_item = count_of_item
        self.item_unit_price = item_unit_price

    def get_purchase_cost_of_items(self):
        """
        Calculates the purchase cost of the item provided to the class
        Returns:
            the product of self.item_unit_price and self.count_of_item
        """
        return self.item_unit_price * self.count_of_item

    def __str__(self):
        """
        Outputs the attributes of the PurchaseItem class and the calculated purchase cost from get_purchase_cost_of_items
        Returns:
            A description of the function attributes and the cost of purchase
        """
        purchase_cost = self.get_purchase_cost_of_items()
        return f"Name: {self.item_name} Count: {self.count_of_item} Unit Price: ${self.item_unit_price:.2f} Purchase Cost ${purchase_cost:.2f}"
