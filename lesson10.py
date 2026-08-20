#Try and catch exceptions

article_input = input("Enter the article number (SKU): ")

try:
    if len(article_input) > 16:
        raise ValueError("Article number cannot be more than 16 digits")
    article_number = article_input.zfill(16)
    print("Article number accepted:", article_number)
except ValueError as e:
    print("Invalid article number:", e)

price_input = input("Enter the retail price (PB00) for this article: ")

try:
    price = float(price_input)
    
    if "." in price_input:
        decimal_part = price_input.split(".")[1]
        if len(decimal_part) > 2:
            raise ValueError("Price cannot have more than 2 decimal places")
    
    print("Price accepted:", price)
except ValueError as e:
    print("Invalid price:", e)

print("Final article record: SKU =", article_number, ", Price =", price)