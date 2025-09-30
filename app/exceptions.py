"""Generic exceptions module"""
class ItemNotFound(Exception):
    """An exception raised when an item is not found"""
    def __init__(self, message: str) -> None:
        super().__init__(*message)