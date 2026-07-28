from read import gain_products, see_products
from operation import sale_product, update_quantity

# Title of the system
def show_title():
    print("-" * 65)
    print("\t\tWeCare Product Wholesale System")
    print("\t\t\tDhapasi, Kathmandu")
    print("\t Treat your skin with our best quality skincare product")
    print("-" * 65)

# main_menu function that runs the program
def main_menu():
    show_title()
    while True:
        print("\n-- WeCare Product Sale System --")
        print("1. Show all the Products")
        print("2. Sell Product")
        print("3. Purchase Product")
        print("4. Leave")

        choose = input("Enter your choice among (1-4): ")

        if choose == "1":
            products_list = gain_products()
            see_products(products_list)
        elif choose == "2":
            products_list = gain_products()
            sale_product(products_list)
        elif choose == "3":
            products_list = gain_products()
            update_quantity(products_list)
        elif choose == "4":
            print("Thank you for visiting our system. Have a good day!")
            break
        else:
            print("Invalid input. Please enter a number between 1-4.")

# it runs the program
if __name__ == "__main__":
    main_menu()
