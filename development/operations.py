from write import sell_bill,purchase_bill
from read import p_dict
    
   
def display_products(is_selling=False):
    print("_"*90)
    print("id\t name \t\t\tbrand \t\t quantity \tprice \torigin")  
    print("_"*90)
    # Iterates through the global p_dict dictionary to print product details
    for p_id, details in p_dict.items():
        price=int(details[3])
        if is_selling:
            display_price=price*2
        else:
            display_price=price
        print(p_id, details[0], details[1], details[2]+"\t\t", str(display_price),details[4])
    print("_"*90)
    print("\n")

def get_valid_phone_number():
     while True:
        phone_number = input("Enter your number:")
        
        if not phone_number.isdigit():
            print("Invalid phone number: Phone number must contain only digits.")
            continue
        
        if len(phone_number) != 10:
            print("Invalid phone number: Phone number must be exactly 10 digits.")
            continue
        return phone_number
    
                


def display_sell():
    """
    Handles the process of selling products, generating a bill, and updating stock.

    This function allows the user to sell products from the inventory. It prompts 
    the customer for their name and phone number, and then iterates through the 
    product list, allowing the customer to select and purchase items. It calculates 
    the total price for each item, applying a free product offer (buy 3, get 1 free), 
    updates the product quantity in the inventory, and displays and generates a bill.

    The following steps are involved in the process:
        1. Prompt for customer details (name and phone number).
        2. Allow the customer to select products and specify quantities.
        3. Validate product ID and quantity.
        4. Calculate the subtotal for each product and update the inventory.
        5. Display the final bill on the screen and save it to a text file with a unique name.

    Raises:
        ValueError: If an invalid product ID or quantity is entered.
    """
    print("\n")
    print("*"*80)
    print("\t\t\t\tSELL PRODUCTS")
    print("*"*80)
    sell_items=[]
    grand_total=0
    display_products()
    #Asking the user to enter values
    name = input("Enter your name:")
    phone_number= get_valid_phone_number()

    #Iterating loop for sell product
    sell_loop = True
    while sell_loop==True: 
        try:
            product_id=int(input("Enter the product ID that you want to buy:"))
            if product_id == 0:
                break
            if product_id <= 0 or product_id > len(p_dict):
                print("Please enter a valid product ID.")
                continue

            
            # Retrieve the product details from the dictionary using the product ID.
            product = p_dict[product_id]
            available_quantity = int(product[2])
            product_quantity=int(input("Please provide the number of quantity you want to buy:"))   

            if product_quantity>available_quantity:
                print("Only"+str(available_quantity)+"units avaliable.Please enter the valid number.")
                continue
            
    
            # Extract the price of the product from the product details (stored as a string) and convert it to an integer.
            price= int(product[3])
            total_cost = price*product_quantity
            free_products=product_quantity//3
            total_quantity=product_quantity+free_products
            
            sell_items.append((product[0], product_quantity, total_quantity, total_cost,free_products))
            grand_total+=total_cost

            p_dict[product_id][2] = str(available_quantity - product_quantity)
            print("Added"+str(product_quantity)+"of"+product[0]+"to the bill.")
        except ValueError:
            print("Invalid input.Please enter the valid input.")
            continue

        add_more=input("Do you want to add more items?(y/n):").lower()
        if add_more=="y" or add_more=="yes":
            continue
        else:
            break
    return name, phone_number, sell_items, grand_total

        
def display_purchase():
    """
    Facilitates the purchase of products from suppliers and updates the inventory.

    This function allows the user to restock items by selecting products, specifying quantities, 
    and calculating the total cost of the purchase. The function performs the following tasks:
    - Collects supplier details (name and phone number).
    - Displays available products to choose from.
    - Updates the inventory with the restocked quantity.
    - Generates a detailed purchase bill and saves it to a uniquely named text file.
    - Displays the purchase details and total cost on the console.

    Key Features:
    - Validates product IDs and input quantities.
    - Calculates subtotal and grand total for the purchase.
    - Supports adding multiple items to the restock list.

    Raises:
    - ValueError: If an invalid input (non-integer or negative value) is provided.
    """
    print("_"*90)
    print("\t\t\t\tPURCHASE PRODUCTS")
    print("_"*90)
    purchase_items=[]
    grand_total_purchase=0
    display_products()
    name = input("Enter the suppliers name:")
    phone_number= get_valid_phone_number()
    purchase_loop = True
    while purchase_loop==True:
        
        try:
            product_id=int(input("Enter the product ID that you want to restock:"))
            if product_id == 0:
                break
            if product_id <= 0 or product_id > len(p_dict):
                print("Please enter a valid product ID.")
                continue

            product = p_dict[product_id]
            unit_price=int(product[3])
            restock_quantity=int(input("Please provide the number of quantity you want to purchase:"))   

            total_cost=unit_price*restock_quantity

            
            purchase_items.append((product[0], restock_quantity, unit_price, total_cost))
            grand_total_purchase+=total_cost

            p_dict[product_id][2] = str(int(p_dict[product_id][2]) + restock_quantity)
            print("Added", restock_quantity, "units of", product[0], "to inventory.")
        except ValueError:
            print("Invalid input.Please enter the valid input.")
            continue

        add_more=input("Do you want to add more items?(y/n):").lower()
        if add_more=="y" or add_more=="yes":
            continue
        else:
            break
    return name, phone_number, purchase_items, grand_total_purchase

        
