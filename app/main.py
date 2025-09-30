"""App main module."""
from helpers import clear_terminal, display_header

def drinks_menu():
    "Drinks Menu function"
    display_header('Drinks Menu')

def baked_goods_menu():
    "Drinks Menu function"
    display_header("Baked Goods Menu")
    

def main_menu() -> dict:
    """
    Main menu for app.
    Returns:
        int: The main menu choice.
    """
    menu_items = {
        1: {
            "name": "Drinks",
            "menu_function": drinks_menu
        },

        2: {
            "name": "Baked Goods",
            "menu_function": baked_goods_menu
        },
        'q': {
            "name": 'Exit',
            "menu_function": lambda: print('Exiting...')
        }
    }
    choice = None
    choice_retries = 0
    for key, value in menu_items.items():
        print(f"{key}: {value['name']}")

    while not choice and choice_retries <= 4:
        choice_retries += 1
        choice = input('Choose a number option from the menu: ')
        try:
            choice = int(choice)
            if choice not in menu_items:
                raise ValueError
        except (TypeError, ValueError):
            if choice_retries == 4:
                print("Retry attempts exceeded.")
                choice = 3
                break
            print(f"Invalid choice '{choice}'. Choose a number option from the menu. \n")
            choice = None

    return menu_items[choice]['menu_function']

def main():
    """Main Menu function"""
    clear_terminal()
    display_header()
    sub_menu = main_menu()
    clear_terminal()
    sub_menu()

if __name__ == "__main__":
    main()