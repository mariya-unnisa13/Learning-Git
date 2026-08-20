# Beginner-friendly Retail Store Program
# Combines: variables, input, math, if/else, loops, lists/dictionaries,
# functions, searching, validation with try/except, and file handling.
#
# Design: a single shared "cart" is used across the whole session.
# Stock is only deducted once, at checkout — not when items are added
# to the cart. This mirrors how a real store works: browsing/adding
# items doesn't commit anything until you actually pay.

FILE_NAME = "products.txt"


def load_products(file_name):
    """Read products from a file and return a list of dictionaries."""
    products = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 4:
                    continue

                sku, name, price, quantity = parts
                try:
                    products.append({
                        "sku": sku,
                        "name": name,
                        "price": float(price),
                        "quantity": int(quantity)
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        products = [
            {"sku": "SKU001", "name": "Milk 4L", "price": 4.99, "quantity": 15},
            {"sku": "SKU002", "name": "Bread", "price": 2.49, "quantity": 20},
            {"sku": "SKU003", "name": "Eggs 12pcs", "price": 3.49, "quantity": 12}
        ]
        save_products(file_name, products)

    if not products:
        products = [
            {"sku": "SKU001", "name": "Milk 4L", "price": 4.99, "quantity": 15},
            {"sku": "SKU002", "name": "Bread", "price": 2.49, "quantity": 20},
            {"sku": "SKU003", "name": "Eggs 12pcs", "price": 3.49, "quantity": 12}
        ]
        save_products(file_name, products)

    return products


def save_products(file_name, products):
    """Write the products list into the file."""
    with open(file_name, "w") as file:
        for product in products:
            file.write(f"{product['sku']},{product['name']},{product['price']},{product['quantity']}\n")


def validate_quantity(value):
    """Accept only positive whole numbers for quantity."""
    try:
        quantity = int(value)
        if quantity <= 0:
            return None
        return quantity
    except ValueError:
        return None


def show_products(products):
    """Display all products."""
    if not products:
        print("No products available.")
        return

    print("\n--- Retail Store Inventory ---")
    for item in products:
        print(f"{item['sku']} | {item['name']} | ${item['price']:.2f} | Qty: {item['quantity']}")


def search_product(products):
    """Find products by name (partial match)."""
    search_text = input("Enter product name to search: ").strip()
    matches = []

    for item in products:
        if search_text.lower() in item["name"].lower():
            matches.append(item)

    if not matches:
        print("No product found.")
        return

    print("\nSearch results:")
    for item in matches:
        print(f"{item['sku']} | {item['name']} | ${item['price']:.2f} | Qty: {item['quantity']}")


def find_product_by_name(products, search_text):
    """Shared helper: partial-match a name against all products.
    Returns None (no match), a single dict (exact one match),
    or asks the user to pick when there are multiple matches."""
    matches = [item for item in products if search_text.lower() in item["name"].lower()]

    if len(matches) == 0:
        print("Product not found.")
        return None

    if len(matches) == 1:
        return matches[0]

    print("Multiple matches found:")
    for i in range(len(matches)):
        print(i + 1, "-", matches[i]["name"])

    choice = input("Enter the number of the correct product: ")
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(matches):
            return matches[choice_index]
    except ValueError:
        pass

    print("Invalid selection.")
    return None


def add_to_cart(products, cart):
    """Add one or more items to the shared cart WITHOUT touching stock yet.
    Stock is only deducted at checkout, once the purchase is final.
    Keeps looping so you can add several products in one go."""
    while True:
        print("\nAdd to Cart")
        name = input("Enter product name (or 'done' to finish adding): ").strip()

        if name.lower() == "done":
            break

        product = find_product_by_name(products, name)
        if product is None:
            continue

        # How much of this item is already sitting in the cart (not yet purchased)
        already_in_cart = sum(c["quantity"] for c in cart if c["sku"] == product["sku"])
        available = product["quantity"] - already_in_cart

        if available <= 0:
            print("This product is out of stock (or fully in your cart already).")
            continue

        while True:
            qty_input = input(f"Enter quantity (available: {available}): ")
            quantity = validate_quantity(qty_input)
            if quantity is None:
                print("Invalid quantity. Please enter a whole number greater than 0.")
                continue
            if quantity > available:
                print(f"Sorry, only {available} left available.")
                continue
            break

        cart.append({
            "sku": product["sku"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

        print(f"Added {quantity} x {product['name']} to cart.")

        add_more = input("Add another product? (yes/no): ").strip().lower()
        if add_more != "yes":
            break


def restock_product(products):
    """Increase the stock quantity of an existing product (e.g. new shipment arrived).
    This is separate from the customer cart — it directly updates inventory."""
    print("\nRestock Product")
    name = input("Enter product name to restock: ").strip()

    product = find_product_by_name(products, name)
    if product is None:
        return

    while True:
        qty_input = input(f"Enter quantity to add (current stock: {product['quantity']}): ")
        quantity = validate_quantity(qty_input)
        if quantity is None:
            print("Invalid quantity. Please enter a whole number greater than 0.")
            continue
        break

    product["quantity"] += quantity
    save_products(FILE_NAME, products)

    print(f"Stock updated: {product['name']} now has {product['quantity']} units.")


def total_bill(cart):
    """Calculate total bill for a customer cart."""
    total = 0.0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total


def checkout(products, cart):
    """Finalize the purchase: deduct stock, print receipt, save to file, clear cart."""
    if not cart:
        print("Your cart is empty. Add something first (option 2).")
        return

    print("\nYour receipt:")
    for item in cart:
        line_total = item["price"] * item["quantity"]
        print(f"{item['name']} x {item['quantity']} = ${line_total:.2f}")

    grand_total = total_bill(cart)
    print(f"\nTotal amount: ${grand_total:.2f}")

    # Only NOW do we actually deduct stock, since the purchase is final
    for cart_item in cart:
        for product in products:
            if product["sku"] == cart_item["sku"]:
                product["quantity"] -= cart_item["quantity"]
                break

    save_products(FILE_NAME, products)
    cart.clear()
    print("Thank you for your purchase! Stock has been updated.")


def view_cart(cart):
    """Show what's currently in the cart (not yet purchased)."""
    if not cart:
        print("Your cart is empty.")
        return

    print("\n--- Current Cart ---")
    for item in cart:
        line_total = item["price"] * item["quantity"]
        print(f"{item['name']} x {item['quantity']} = ${line_total:.2f}")
    print(f"Cart total so far: ${total_bill(cart):.2f}")


def main():
    """Main menu of the retail store application."""
    products = load_products(FILE_NAME)
    cart = []  # shared cart, lives for the whole session

    print("Welcome to the Beginner Retail Store!")

    while True:
        print("\nMenu:")
        print("1. View products")
        print("2. Add to cart")
        print("3. Search product")
        print("4. View cart")
        print("5. Checkout")
        print("6. Restock product (add stock)")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            show_products(products)
        elif choice == "2":
            add_to_cart(products, cart)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            checkout(products, cart)
        elif choice == "6":
            restock_product(products)
        elif choice == "7":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")


main()