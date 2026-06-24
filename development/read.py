
p_dict={}
def load_products():
    """
    Loads product data from a file and stores it in a global dictionary.

    This function reads product data from the file "products.txt". Each line in 
    the file is expected to contain product information in a comma-separated 
    format. The function splits each line into product details and stores them 
    in a global dictionary, where the key is a unique product ID, and the value 
    is a list of product details.

    The global dictionary `p_dict` is updated with new entries for each product.

    Returns:
        None
    """

    #Declaring a global variable
    global p_dict 
    file=open("products.txt","r")
    # Read all lines from the file and store them as a list in p_data.
    p_data= file.readlines()
    p_id = 1
    for line in p_data:
        """Remove the newline character from the end of the line and then split the line into a list
        of values based on the comma ."""
        line = line.replace("\n","").split(",")
        p_dict[p_id] = line
        p_id=p_id+1
    file.close()
