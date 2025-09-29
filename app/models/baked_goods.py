class BakedGood:
    """
    A class Representing a baked good product.

    Attributes:
        name (str): The product's name.
        vendor_name (str): The product's vendor.
        purchasing_cost (float): The product's unit cost.
        markup_percentage (float): The purchase cost multiplier.
        known_allergens (list[str]): A list of known allergens in the product's ingredients.
        count (int): The amount of available units for this product.
    """

    def __init__(self, name: str, vendor_name: str, purchasing_cost: float, markup_percentage: float, known_allergens: list[str], count: int) -> None:
        """Initializes this object.
        Args:
            name (str): The product's name.
            vendor_name (str): The product's vendor.
            purchasing_cost (float): The product's unit cost.
            markup_percentage (float): The purchase cost multiplier.
            known_allergens (list[str]): A list of known allergens in the product's ingredients.
            count (int): The amount of available units for this product.
        """
        self._name: str = name
        self._vendor_name: str = vendor_name
        self._purchasing_cost: float = purchasing_cost
        self._markup_percentage: float = markup_percentage
        self._known_allergens: list[str] = known_allergens
        self._count: int = count

    @property
    def name(self) -> str:
        """str: The product's name."""
        return self._name

    @property
    def vendor_name(self) -> str:
        """str: The product's vendor name."""
        return self._vendor_name

    @property
    def purchasing_cost(self) -> float:
        """float: The base purchasing cost of the product."""
        return self._purchasing_cost

    @property
    def markup_percentage(self) -> float:
        """float: The markup percentage applied to the purchasing cost."""
        return self._markup_percentage

    @property
    def known_allergens(self) -> list[str]:
        """list[str]: Known allergens contained in the product."""
        return self._known_allergens

    @property
    def count(self) -> int:
        """int: The number of available units of the product."""
        return self._count

