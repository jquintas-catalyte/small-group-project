"""App main module."""
import sys
from services import DrinkService, BakedGoodsService, IngredientService
from repositories import DrinkRepository, BakedGoodsRepository, IngredientRepository
from helpers import display_menu, clear_terminal, display_header

ingredients_service = IngredientService(IngredientRepository())
baked_goods_service = BakedGoodsService(BakedGoodsRepository())
drinks_service = DrinkService(DrinkRepository())

def drinks_menu():
    "Drinks Menu function"
    display_header('Drinks Menu')

def baked_goods_menu():
    "Drinks Menu function"
    display_header("Baked Goods Menu")

def inventory_menu():
    "Displays Inventory"
    clear_terminal()
    display_header('Inventory')
    menu_choice  = display_menu({"1": "Baked Goods", "2": "Ingredients", "q": "Main Menu"})
    if not menu_choice:
        menu_choice = "q"
    if menu_choice == "q":
        main_menu()
        return
    if menu_choice == "1":
        baked_goods_inventory()
        return
    ingredients_inventory()
    
def ingredients_inventory():
    "Displays Ingredients inventory"
    display_header("Inventory - Ingredients")
    ingredients = ingredients_service.get_all()
    for idx, item in enumerate(ingredients):
        print(f"{idx + 1}: {item}")


def baked_goods_inventory():
    "Displays Baked goods inventory"
    display_header("Inventory - Baked Goods")
    products = baked_goods_service.list_products()
    for idx, product in enumerate(products):
        print(f"{idx + 1}: {product}")


def main_menu():
    """
    Main menu for app.
    Returns:
        int: The main menu choice.
    """
    clear_terminal()
    display_header('Main Menu')

    menu_items = {
        "1": "Inventory",
        "2": "Baked Goods Menu",
        "3": "Drinks Menu",
        "q": "Exit",
    }
    main_choice =  display_menu(menu_items)
    if not main_choice or main_choice == "q":
        print('Exiting...')
        sys.exit(0)
        return lambda: ...
    
    if main_choice == "1":
        inventory_menu()
        return
    if main_choice == "2":
        baked_goods_menu()
        return
    return drinks_menu


def main():
    """Main Menu function"""
    clear_terminal()
    main_menu()

if __name__ == "__main__":
    main()