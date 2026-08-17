#Combining lists and dictionaries
articles=[
    {"sku":"61078273867", "name": "Milk 4L", "price": 3.99},
    {"sku":"61078273868", "name": "Bread 1KG", "price": 2.49},
    {"sku":"61078273869", "name": "Eggs 12pcs", "price": 3.49}
]

for item in articles:
    print(item["sku"], "-", item["name"], "$", item["price"])

