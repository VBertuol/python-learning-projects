def add_product(products, code, name, quantity, price):
    products.append({"code": code, "name": name, "quantity": quantity, "price": price})

def list_all_products(products):
    for product in products:
        print(f"Code: {product['code']}, Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")

def search_product_by_code(products, code):
    return next((p for p in products if p["code"] == code), None)

def remove_product(products, code):
    return [p for p in products if p["code"] != code]

def load_data(filename):
    products = []
    try:
        with open(filename, "r") as file:
            for line in file:
                code, name, quantity, price = line.strip().split(",")
                products.append({"code": code, "name": name, "quantity": int(quantity), "price": float(price)})
    except FileNotFoundError:
        pass
    return products

def save_data(filename, products):
    with open(filename, "w") as file:
        for product in products:
            file.write(f"{product['code']},{product['name']},{product['quantity']},{product['price']}\n")

def validate_numeric_input(value, type_):
    try:
        return type_(value)
    except ValueError:
        return None

def update_product_quantity(products, code, quantity_change):
    product = search_product_by_code(products, code)
    if product:
        product["quantity"] += quantity_change
        return True
    return False

def sort_products(products, key="name"):
    return sorted(products, key=lambda x: x[key])

def display_menu():
    print("\nMenu:")
    print("1. Add Product")
    print("2. List Products")
    print("3. Search Product by Code")
    print("4. Remove Product")
    print("5. Update Quantity")
    print("6. Exit")

def main():
    filename = "inventory.txt"
    products = load_data(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            code = input("Enter product code: ")
            name = input("Enter product name: ")
            quantity = validate_numeric_input(input("Enter quantity: "), int)
            price = validate_numeric_input(input("Enter price: "), float)

            if quantity is not None and price is not None:
                add_product(products, code, name, quantity, price)
            else:
                print("Invalid input. Product not added.")

        elif choice == "2":
            sorted_key = input("Sort by (name/price): ").strip().lower()
            if sorted_key in ["name", "price"]:
                products = sort_products(products, key=sorted_key)
            list_all_products(products)

        elif choice == "3":
            code = input("Enter product code to search: ")
            product = search_product_by_code(products, code)
            if product:
                print(f"Found: Code: {product['code']}, Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")
            else:
                print("Product not found.")

        elif choice == "4":
            code = input("Enter product code to remove: ")
            products = remove_product(products, code)

        elif choice == "5":
            code = input("Enter product code to update: ")
            quantity_change = validate_numeric_input(input("Enter quantity change (+/-): "), int)
            if quantity_change is not None:
                if update_product_quantity(products, code, quantity_change):
                    print("Quantity updated.")
                else:
                    print("Product not found.")

        elif choice == "6":
            save_data(filename, products)
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
