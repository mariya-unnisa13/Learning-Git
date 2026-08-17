#Dictionaries- key-value pairs

article={
    "sku":"61078273867",
    "name": "Milk 4L",
    "price": 3.99
}

print("the article sku is:", article["sku"])
print("the article name is:", article["name"])
print("the article price is:", article["price"])

for key in article:
    print(key, ":", article[key])