import datetime

# saves products to file
def save_products(products_list):
    with open("productlist.txt", "w") as f:
        for product in products_list:
            line = str(product['id'])+ "," +product['name']+ "," +str(product['price'])+ "," +product['company']+ "," +str(product['quantity'])+ "," +product['country'] + "\n"
            f.write(line)

# Invoice print
def invoice_sale(products, sale_invoice, customer_name_s, customer_address_s, customer_number_s):
    print("\n---- Customer Invoice ----")
    print("Customer Name:", customer_name_s)
    print("Address:      ", customer_address_s)
    print("Phone Number: ", customer_number_s)
    print("Date:         ", str(datetime.date.today()))
    print("-" * 55)
    
    print("Product       Qty   Free   Price")
    total = 0
    for prod in products:
        name = prod[0]
        qty = str(prod[1])
        free_item = str(prod[2])
        price = str(prod[3])
        displayed = name + " " *(15 - len(name)) + qty + " " * (6 - len(qty)) + free_item + " " * (6 - len(qty)) + price + " " * (10 - len(price))
        print(displayed)
        total += int(prod[3])

    print("-" * 55)
    print("Total price: Rs", total)
    # Save invoice to file
    try:
        file = open("saleinvoice.txt", "w")
        file.write("Name of Customer: " + customer_name_s + "\n")
        file.write("Address: " + customer_address_s + "\n")
        file.write("Phone Number: " + customer_number_s + "\n")
        file.write("Date: " + str(datetime.date.today()) + "\n\n")
        for product in products:
            outputresult_s = product[0] + " Qty: " + str(product[1]) + ", FreeItem: " + str(product[2]) + ", Price: " + str(product[3])
            file.write(outputresult_s + "\n")
        file.write("\n")
        file.close()
    except:
        print("Error writing invoice file.")

#purchase
def invoice_purchase(products, purchase_invoice, customer_name_p, customer_address_p, customer_number_p):
    print("\n---- Customer Invoice ----")
    print("Customer Name:", customer_name_p)
    print("Address:      ", customer_address_p)
    print("Phone Number: ", customer_number_p)
    print("Date:         ", str(datetime.date.today()))
    print("-" * 55)
    
    print("Product        Qty Added")
    total_qty = 0
    for prod in products:
        name = prod[0]
        qty = str(prod[1])
        displays = name + " " *(15 - len(name)) + qty + " " * (6 - len(qty)) 
        print(displays)
        total_qty += int(prod[1])

    print("-" * 55)
    print("Total Quantity of Product:", total_qty)
    # Save invoice to file
    try:
        file = open("purchaseinvoice.txt", "w")
        file.write("Name of Customer: " + customer_name_p + "\n")
        file.write("Address: " + customer_address_p + "\n")
        file.write("Phone Number: " + customer_number_p + "\n")
        file.write("Date: " + str(datetime.date.today()) + "\n\n")
        
        for product in products:
            outputresult_p = product[0] + " Qty Added: " + str(product[1])
            file.write(outputresult_p + "\n")
        file.write("\n")
        file.close()
    except:
        print("Error writing invoice file.")
