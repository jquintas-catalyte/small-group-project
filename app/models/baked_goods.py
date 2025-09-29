class BakedGood:
    """
    A class Representing a baked good product.
    Attributes:
        name (str): The products name.
        vendor_name (str): The product's vendor.
        purchasing_cost (float): The product's unit cost.
        markup_percentage (float): The purchase cost multiplier.
        known_allergens (list[str]): A list of known allergens in the product's ingredients.
        count (int): The amount of available units for this product.
    """

    def __init__(self, name: str, vendor_name: str, purchasing_cost: float, markup_percentage: float, known_allergens: list[str], count: int) -> None:
        """ Initializes this object.
        Args:
            name (str): The products name.
            vendor_name (str): The product's vendor.
            purchasing_cost (float): The product's unit cost.
            markup_percentage (float): The purchase cost multiplier.
            known_allergens (list[str]): A list of known allergens in the product's ingredients.
            count (int): The amount of available units for this product.
        """

