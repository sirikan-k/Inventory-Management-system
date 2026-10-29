def update_stock(products):
    products_id = input("Enter product id")

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
        if keyword == product["id"] or keyword == product["name"]:
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