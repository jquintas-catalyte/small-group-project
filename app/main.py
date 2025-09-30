"""App entry module."""

def menu():
    print('Main menu')
    print("1. Drinks")
    print("2. Baked Goods")
    choice = int(input('Choose an option: '))
    print(choice)

def main():
    """Main function"""
    print('Express-O Artisan Coffee')
    menu()

if __name__ == "__main__":
    main()