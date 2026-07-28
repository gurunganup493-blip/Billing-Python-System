from read import see_products
from write import save_products, invoice_sale, invoice_purchase

# Selling the product
def sale_product(products_list):
    if not products_list:
        print("No products to sell.")
        return

    sold_products = []
    customer_name_s = input("Enter customer name: ")
    customer_address_s = input("Enter customer address: ")
    customer_number_s = input("Enter customer phone number: ")
    while not customer_number_s.isdigit():
        customer_number_s = input("Please enter a valid phone number in digits: ")

    while True:
        print("\n Available Products for Sale:")
        see_products(products_list)
        print()
        
        # Ask until valid product ID is entered
        while True:
            try:
                productid = int(input("Enter product ID to sell (0 to exit): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid product ID number.")

        if productid == 0:
            break
        
        found = False
        for product in products_list:
            if product["id"] == productid:
                found = True
                while True:
                    try:
                        quantity = int(input("Enter quantity to sell (Available Now: " + str(product['quantity'])+"):"))
                        if quantity < 0:
                            print("Quantity must be always positive.")
                            continue
                        if quantity > product["quantity"]:
                            print("Not enough stock.")
                            continue
                        
                        free_items = quantity // 3
                        total_need = quantity + free_items

                        if total_need > product["quantity"]:
                            print("Not enough stock. You need", total_need, "quantity of that product, but only", product["quantity"], "available.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid quantity.")
                        
                product["quantity"] -= total_need
                total_price = product["price"] * quantity
                print("Sold", quantity, "quantity of", product["name"], ". Total price: Rs", round(total_price,2))
                save_products(products_list)
                        
                if quantity >= 3:
                    print("You got", free_items, "free items as a special offer!")
                sold_products.append([product["name"], quantity, free_items, total_price])
                break
                    
        if not found:
            print("Product not found. Please enter a valid product ID number.")
            continue

        while True:
            extra = input("Do you want to sell more products? (yes/no): ").lower()
            if extra == 'yes':
                break

            elif extra == 'no':
                invoice_sale(sold_products, "Invoice of Sale", customer_name_s, customer_address_s, customer_number_s)
                print("Thank you.")
                return
                    
            else:
                print("Invalid input.Type yes or no for further process.")


# Update quantity
def update_quantity(products_list):
    if not products_list:
        print("No products available.")
        return

    products_purchased = []
    customer_name_p = input("Enter customer name: ")
    customer_address_p = input("Enter customer address: ")
    customer_number_p = input("Enter customer phone number: ")
    while not customer_number_p.isdigit():
        customer_number_p = input("Please enter a valid phone number in digits: ")

    while True:
        print("\n Available Products:")
        see_products(products_list)
        print()

        while True:
            try:
                productid = int(input("Enter product ID to purchase (0 to exit): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid product ID.")

        if productid == 0:
                break
                
        found = False
        for product in products_list:
            if product["id"] == productid:
                found = True
                print("Current Quantity:", product["quantity"])
                while True:
                    try:
                        new_quantity = int(input("Enter new quantity to add: "))
                        if new_quantity < 0:
                            print("Quantity cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid quantity.")

                product["quantity"] += new_quantity
                save_products(products_list)
                        
                print("Successfully added", new_quantity, "items. New quantity:", product["quantity"])
                products_purchased.append([product["name"], new_quantity])
                break
                        
        if not found:
            print("Product not found. Please enter a valid product ID number.")
            continue
        
        while True:
            extra = input("Do you want to sell more products? (yes/no): ").lower()
            if extra == 'yes':
                break

            elif extra == 'no':
                invoice_purchase(products_purchased, "Invoice of Purchase", customer_name_p, customer_address_p, customer_number_p)
                print("Thank you.")
                return
                    
            else:
                print("Invalid input.Type yes or no for further process.")
