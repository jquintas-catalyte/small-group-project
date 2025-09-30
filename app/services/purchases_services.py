""" Definition of Purchase Services """
from ..repositories import purchases_repository

class PurchaseServices:
    
	def __init__ (self) -> None:
		self.purchases_repository = purchases_repository([])


