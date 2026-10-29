#!/usr/bin/env python3

products = [
    {
        "id": "P001",
        "name": "Pen",
        "price": 10.0,
        "quantity": 5
    },
    {
        "id": "P002",
        "name": "Book",
        "price": 50.0,
        "quantity": 20
    },
    {
        "id": "P003",
        "name": "pencil",
        "price": 5.0,
        "quantity": 10
    },
    {
        "id": "P004",
        "name": "Eraser",
        "price": 5.0,
        "quantity": 15
    },
    {
        "id": "P005",
        "name": "Ruler",
        "price": 12.0,
        "quantity": 10
    },
    {
        "id": "P006",
        "name": "Notebook",
        "price": 30.0,
        "quantity": 12
    },
    {
        "id": "P007",
        "name": "Marker",
        "price": 20.0,
        "quantity": 7
    },
    {
        "id": "P008",
        "name": "Glue",
        "price": 15.0,
        "quantity": 20
    },
    {
        "id": "P009",
        "name": "Stapler",
        "price": 40.0,
        "quantity": 8
    },
    {
        "id": "P010",
        "name": "Scissors",
        "price": 30.0,
        "quantity": 8
    }
]

def show_menu():
    print("===== Inventory Management=====")
    print("1. Add product")
    print("2. View prodcut")
    print("3. Update stock")
    print("4. Search product")
    print("5. Stock summary")
    print("6. Remove product")
    print("7. Exit")

def add_product(products):
    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Product added successfully!")

def view_product(products):
    if not products:
        print("Not ptoducts found")
    else:
        print("ID | Name | Price | Quantity")

        for product in products:
            print(
                product["id"], "|",
                product["name"], "|" ,
                product["price"], "|",
                product["quantity"]  
            )

def update_stock(products):
    products_id = input("Enter product id: ")

    for product in products:
        if product["id"] == products_id:
            print("1. Add stock")
            print("2. Reduce stock")

            choice = input("Choose option: ")
            amount = int(input("Enter quatity: "))

            if amount <= 0:
                print("Quantity must be positive: ")
                return
            if choice == "1":
                product["quantity"] += amount
                print("Stock updated successfully")
            elif choice == "2":
                if amount <= product["quantity"]:
                    product["quantity"] -= amount
                    print("Stock updated successfully")
                else:
                    print("Not enough stock")
            else:
                print("Invalid option")
            return
    print("Product not found")


def search_product(products, keyword):
    for product in products:
        if (keyword.lower() == product["id"].lower() or keyword.lower() == product["name"].lower()):
            return product
    return None

def stock_summary(products):
    total_value = 0

    print("\n --- Stock Summary ---")

    for product in products:
        value = product["price"] * product["quantity"]
        total_value += value

        if product["quantity"] <= 5:
            print("Low stock:", product["name"], "-", product["quantity"], "left")

    print("Total stock value: ", total_value, "baht")

def remove_product(products):
    product_id = input("Enter product id to remove: ")
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Product removed successfully")
            return
    print("Product not found")

while True:
    show_menu()
    choice = input("Enter your menu: ")

    if choice == "1":
        add_product(products)

    elif choice == "2":
        view_product(products)

    elif choice == "3":
        update_stock(products)

    elif choice == "4":
        keyword = input("Enter product id or name: ")
        result = search_product(products, keyword)
        if result is not None:
            print(result)
        else:
            print("Product not found")

    elif choice == "5":
        stock_summary(products)

    elif choice == "6":
        remove_product(products)

    elif choice == "7":
        print("Exit program")
        break

    else:
        print("Invalid choice")


    
    
