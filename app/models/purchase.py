from datetime import datetime
from zoneinfo import ZoneInfo

class Purchase:
    
    next_order_id = 1

    @staticmethod
    def _get_time():
        chicago_time_now = datetime.now(tz=ZoneInfo("America/Chicago"))
        return chicago_time_now.strftime("%Y-%m-%d %H:%M:%S %Z")
    
    
    def __init__(self, items: list, status: str, prices: float):
        self.items = items
        self.status = status
        self.prices = prices
        
        self.purchase_id = Purchase.next_order_id
        Purchase.next_order_id += 1

        self.purchase_date = Purchase._get_time()

    def get_order(self):
        """Returns the items and the unique order number."""
        return self.items, self.purchase_id

    

    
        
    

                
            
