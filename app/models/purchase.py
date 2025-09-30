""" Defintion of Purchases """
from datetime import datetime
from zoneinfo import ZoneInfo
from .purchase_item import PurchaseItem
    
class Purchase:

    next_order_id = 1

    def __init__(self, purchase_id:  int | None=None, status:str = 'unpaid', items: list[PurchaseItem] = [], date: str | None = None):
        """ Initializes a new coffee shop order.
        It sets up the order with default values and assigns a unique.
        ID and the creation timestamp.
        """
        self.items = items
        self.status: str = status     
        if not purchase_id:
            self.purchase_id: int = Purchase.next_order_id
            Purchase.next_order_id += 1
        else:
            self.purchase_id =  purchase_id
        
        self.purchase_date = date or Purchase.get_time()
    
    def __repr__(self):
        return (f"Purchase(items={self.items!r}, " 
                f"status={self.status!r}, "
                f"date={self.purchase_date!r}, "
                f"order_id={self.purchase_id!r})")

    def get_order(self):
        """ Returns the items and the unique order number """
        return self.items, self.purchase_id
    
    def total_cost(self):
        """ Returns the total cost of all the items purchased """
        final_total = 0
        for item in self.items:
            final_total += item.get_purchase_cost_of_items()
        return final_total
    
    def add_item(self, item: PurchaseItem):
        """ Add item to the list """
        self.items.append(item)

    @staticmethod
    def get_time():
        """ Returns time in Chicago Standard Time """
        chicago_time_now = datetime.now(tz=ZoneInfo("America/Chicago"))
        return chicago_time_now.strftime("%Y-%m-%d %H:%M:%S %Z")
    

    
        

            
