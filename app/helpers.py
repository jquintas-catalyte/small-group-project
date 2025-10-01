"""A collection of helper functions"""
import os
def clear_terminal():
    """Clears the terminal/ command line."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(choices: dict[str, str], retries: int = 5):
    """Displays menu choices and return choice"""
    choice = None
    choice_retries = 0
    for key, value in choices.items():
        print(f"{key}: {value}")

    while not choice and choice_retries <= retries:
        choice_retries += 1
        choice = input('Choose a number option from the menu: ')
        try:
            if choice not in choices:
                raise ValueError
        except ValueError:
            choice = None
            if choice_retries == 4:
                print("Retry attempts exceeded.")
                break
            print(f"Invalid choice '{choice}'. Choose a number option from the menu. \n")
    return choice


def display_header(sub_menu: str | None = None):
    """Prints the company header."""
    header = f"Express-O Coffee Shop{": " + sub_menu if sub_menu else ''}"
    divider = '-' + ''.join(['-' for _ in header]) + '-'
    print(f"{divider}\n{header}\n{divider}")

