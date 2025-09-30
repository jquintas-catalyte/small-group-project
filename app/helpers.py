"""A collection of helper functions"""
import os
def clear_terminal():
    """Clears the terminal/ command line."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(sub_menu: str | None = None):
    """Prints the company header."""
    header = f"Express-O Coffee Shop{": " + sub_menu if sub_menu else ''}"
    divider = '-' + ''.join(['-' for _ in header]) + '-'
    print(f"{divider}\n{header}\n{divider}")