#Wrapping validations in functions. These functions are used to validate user input and ensure that the data being processed meets certain criteria. They can check for valid formats, ranges, and other conditions, and return appropriate messages or prompts to guide the user in providing correct input.

#adding None if the return statement fails
def validate_article(article_input):
    if len(article_input) > 16:
        return None
    return article_input.zfill(16)

def validate_price(price_input):
    try:
        price = float(price_input)
    except ValueError:
        return None
    
    if price <= 0:
        return None
    
    if "." in price_input:
        decimal_part = price_input.split(".")[1]
        if len(decimal_part) > 2:
            return None
    
    return price


article_number = None
while article_number is None:
    article_input = input("Enter the article number (SKU): ")
    article_number = validate_article(article_input)
    if article_number is None:
        print("Invalid article number — cannot be more than 16 digits")

print("Article number accepted:", article_number)

#article is valid
price = None
while price is None:
    price_input = input("Enter the retail price (PB00) for this article: ")
    price = validate_price(price_input)
    if price is None:
        print("Invalid price — must be numeric with max 2 decimal places")

print("Final article record: SKU =", article_number, ", Price =", price)