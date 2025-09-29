from datetime import datetime
from zoneinfo import ZoneInfo

class Purchase:
    

    @staticmethod
    def date_and_time():
        chicago_time_now = datetime.now(tz=ZoneInfo("America/Chicago"))
        return chicago_time_now.strftime("%Y-%m-%d %H:%M:%S %Z")
    
    
    def __init__(self, items, status, prices):
        self.items = items
        self.status = status
        self.prices = prices
        
        self.purchase_idpurchase_id = 1

    

    
        
    

                
            
