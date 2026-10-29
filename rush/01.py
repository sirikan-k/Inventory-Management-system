def show_menu():
    print("\n=====Inventonry Management=====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Stock Summary ")
    print("6. Remove Product")
    print("0. Exit")

def main():
    while True :
        show_menu()
        choice = (input("Choose menu: "))

        if choice == "1":
            print("Add Product")
        elif choice == "2":
            print("View Products")
        elif choice == "3":
            print("Update Stock")
        elif choice == "4":
            print("Search Product")
        elif choice == "5":
            print("Stock Summary")
        elif choice == "6":
            print("Remove Product")
        elif choice == "0":
            print("Exit")
            break
        else:
            print("Invalid menu. Please try again.")
    
products = []

def show_menu():
    print("Add Product")
    print("View Products")
    print("Update Stock")
    print("Search Product")
    print("Stock Smmary")
    print("Remove Product")
    print("Exit")

def add_product(products):
    product_id = input("Enter product id : ")
    name = input("Enter product name: ")
    price = float(input("Enter produt price: "))
    quantity = int(input("Enter produt quntity: "))

    product = { 
        "id": product_id,
        "name": name,
        "price": price,
        "quantiity": quantity,
    }
    
    products.append(product)
    print("Product added successfully!")

def shoe_menu():
    print("1. Add Product")
    print("2. View Products")
    print("Update Stock")
    print("Search Product")
    print("Stock Smmary")
    print("Remove Product")
    print("Exit")



