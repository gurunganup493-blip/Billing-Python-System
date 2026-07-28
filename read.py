# create a text file with some products and their details
def sample_file():
    details = """1,Lip Balm,50,Sancho,501,Nepal
2,Facewash,180,Himalaya,460,India
3,Lotion,650,Johnson Baby,669,USA
4,Face Mask,510,Asarai,574,AUS
5,Hair Oil,50.0,Clear,744,Sri Lanka
6,Hand wash,80.0,Dettol,580,Bangladesh"""
    with open("productlist.txt", "w") as file:
        for line in details.split("\n"):
            file.write(line + "\n")

# Title of the system
def show_title():
    print("-" * 65)
    print("\t\tWeCare Product Wholesale System")
    print("\t\t\tDhapasi, Kathmandu")
    print("\t Treat your skin with our best quality skincare product")
    print("-" * 65)
    
# reads the details of product from the file
def gain_products():
    products_list = []
    try:
        with open("productlist.txt", "r") as file:
            for line in file:
                #skips empty and blank lines
                if line != "\n":
                    productid, name, price, company, qty, country = line.split(",")
                    # Creating a dictionary for each product
                    products = {"id": int(productid),"name": name, "price": float(price), "company": company, "quantity": int(qty), "country": country}
                    products_list.append(products)
        return products_list
    except FileNotFoundError:
        print("File not found! Make sure 'productlist.txt' exists.")
        return []
    except Exception as e:
        print("Error. Something went wrong:", e)
        return []

# Displaying the list of products in a readable format
def see_products(products_list):
    if not products_list:
        print("No product details available.")
        return

    print("\n WeCare Product Wholesale Catalog ")
    print("Id   Name           Price     Company        Qty   Country")
    print("-" * 65)

    for p in products_list:
        id = str(p['id'])
        name = p['name']
        price = "Rs " + str(int(p['price']))
        company = p['company']
        qty = str(p['quantity'])
        country = p['country']

        # Fixed-width column padding using space repetition
        id_column = id + " " * (5 - len(id))
        name_column = name + " " * (15 - len(name))
        price_column = price + " " * (10 - len(price))
        company_column = company + " " * (15 - len(company))
        qty_column = qty + " " * (6 - len(qty))
        country_column = country

        print(id_column + name_column + price_column + company_column + qty_column + country_column)
