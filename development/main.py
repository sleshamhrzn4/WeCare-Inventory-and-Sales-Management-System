from read import load_products
from operations import display_products, display_sell, display_purchase
from write import sell_bill, purchase_bill

# Printing all the additional information
print("\n")
print("\t\t\t\t WECARE WHOLESALE ")
print("\t\t\t\t Kamalpokhari, Kathmandu")
print("\t\t\t\t Phone No: 9866337738")
print("\n")
print("\t\t\t\t WELCOME TO THE SYSTEM!!!")
print("\n")


def display_menu():
    """
    Parameters:
        None

    Function:
        Prints the menu options available to the user for interacting with the WeCare Wholesale system.

    Returns:
        None
    """
    # Providing lines for design purpose
    print("_" * 90)
    print("Here are some of the choices for you to carry out the needed operation in the system.")
    print("_" * 90)
    # Printing all the options
    print("1) Display Products")
    print("2) Sell product")
    print("3) Purchase product")
    print("4) Exit")
    print("_" * 90)


def main():
    """
    Parameters:
        None

    Function:
        Manages the main workflow of the WeCare Wholesale system:
        - Loads product data from the inventory.
        - Displays menu options to the user.
        - Handles user choices and calls appropriate functions to display products, handle sales, or manage purchases.

    Returns:
        None
    """
    load_products()
    while True:
        display_menu()
        choice = input("Enter your choice:")

        if choice == "1":
            display_products()
        elif choice == "2":
            name, phone_number, sell_items, grand_total = display_sell()
            sell_bill(name, phone_number, sell_items, grand_total)

        elif choice == "3":
            name, phone_number, purchase_items, grand_total_purchase = display_purchase()
            purchase_bill(name, phone_number, purchase_items, grand_total_purchase)
        elif choice == "4":
            print("The system is exiting. Thank you for visiting.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")


if __name__ == "__main__":
    main()
