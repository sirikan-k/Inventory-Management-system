products = [
    {
        "id": "P001",
        "name": "Pen",
        "price": 10,
        "quantity": 5
    },
    {
        "id": "P002",
        "name": "Book",
        "price": 50,
        "quantity": 20
    },
    {
        "id": "P003",
        "name": "pencil",
        "price": 5,
        "quantity": 10
    },
    {
        "id": "P004",
        "name": "Eraser",
        "price": 5,
        "quantity": 15
    },
    {
        "id": "P005",
        "name": "Ruler",
        "price": 12,
        "quantity": 10
    },
    {
        "id": "P006",
        "name": "Notebook",
        "price": 30,
        "quantity": 12
    },
    {
        "id": "P007",
        "name": "Marker",
        "price": 20,
        "quantity": 7
    },
    {
        "id": "P008",
        "name": "Glue",
        "price": 15,
        "quantity": 20
    },
    {
        "id": "P009",
        "name": "Stapler",
        "price": 40,
        "quantity": 8
    },
    {
        "id": "P010",
        "name": "Scissors",
        "price": 30,
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

def add_product():
    product_id = input("Enter product ID: ")

    for product in products:
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

def view_product():
    if not products:
        print("Not ptoducts found")
    else:
        print("ID | Name | Price | Quantity")

        for product in products:
            print(
                product["id"], "|",
                product["name"], "|" ,
                product["price"], "|",
                product["quantity"], "|",  
            )

while True:
    show_menu()
    choice = input("Enter your menu: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_product()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        search_product()

    elif choice == "5":
        stock_summary()

    elif choice == "6":
        remove_product()

    elif choice == "7":
        print("Exit program")
        break

    else:
        print("Invalid choice")


    
    
