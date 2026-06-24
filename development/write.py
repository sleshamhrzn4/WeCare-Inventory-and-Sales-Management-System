import datetime

def unique_file():
# Get the current year, month, day, hour, minute, and second from the current date and time.   
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    hour=str(datetime.datetime.now().hour)
    minute=str(datetime.datetime.now().minute)
    second=str(datetime.datetime.now().second)

    # Combine the year, month, day, hour, minute, and second into a unique string.
    unique_num=year+month+day+hour+minute+second
    # Create the file name by appending ".txt" to the unique string.
    file_name=unique_num+".txt"
    return file_name

def sell_bill(name, phone_number, sell_items, grand_total):
    file_name=unique_file()
    file=open(file_name,"w")
    
    file.write("----------Purchased Order Bill--------\n")
    file.write("Customer's name:" + name +"\n")
    file.write("Phone number:"+ phone_number+"\n")
    file.write("Product Details:\n")
    print("-" * 30)
    
    for item in sell_items:
        file.write("Product: " + item[0]+"\n")
        file.write("Quantity: " + str(item[1])+"\n")
        file.write("Free Products:"+str(item[4])+"\n")
        file.write("Total Quantity: " + str(item[2])+"\n")
        file.write("Subtotal: " + str(item[3])+"\n")
        file.write("-" * 30+"\n")
        
    file.write("Grand Total: " + str(grand_total)+"\n")
    file.write("-"*30+"\n")
    
    print("Bill")
    print("-"*30)
    print("Customer's name:"+name)
    print("Phone number:"+phone_number)
    print("Product Details:")
    for item in sell_items:
        print("Product: " + item[0])
        print("Quantity: " + str(item[1]))
        print("Free Products:"+str(item[4]))
        print("Total Quantity: " + str(item[2]))
        print("Subtotal: " + str(item[3]))
        print("-" * 30)
    
        
    print("Grand Total: " + str(grand_total))
    print("-"*30)


def purchase_bill(name, phone_number, purchase_items, grand_total_purchase):  
    file_name=unique_file()
    file=open(file_name,"w")
    
    file.write("----------Purchased Order Bill--------\n")
    file.write("Supplier's name: " + name + "\n")
    file.write("Supplier's phone number: " + phone_number + "\n")
    file.write("-" * 30 + "\n") 
    file.write("Product Details:\n")
    file.write("-" * 30 + "\n") 
    for item in purchase_items:
        file.write("Product: " + item[0] + "\n")
        file.write("Quantity: " + str(item[1]) + "\n")
        file.write("Unit Price: " + str(item[2]) + "\n")
        file.write("Subtotal: " + str(item[3]) + "\n")
        file.write("-" * 30 + "\n")  
    file.write("Grand Total: " + str(grand_total_purchase) + "\n")

    # Print purchase details to the console
    print("-"*30)
    print("Purchase Order")
    print("-"*30)
    print("Supplier's name: " + name)
    print("Supplier's phone number: " + phone_number)
    print("Product Details:")
    for item in purchase_items:
        print("Product: " + item[0])
        print("Quantity: " + str(item[1]))
        print("Unit Price: " + str(item[2]))
        print("Subtotal: " + str(item[3]))
        print("-" * 30)
    print("Grand Total: " + str(grand_total_purchase))
    print("-" * 30)   


    
