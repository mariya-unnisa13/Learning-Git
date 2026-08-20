#File Handling(reading and writing files)

articles = [
    {"sku": "0000000000000104", "name": "Farmers Reg Milk 2L", "price": 4.99},
    {"sku": "0000000000000140", "name": "Oat Milk 2L", "price": 5.29}
]

# Writing to a file
with open("articles.txt", "w") as file:
    for item in articles:
        file.write(f"{item['sku']},{item['name']},{item['price']}")

print("Articles saved to file")

#Reading from a file
with open("articles.txt", "r") as file:
    for line in file:
        print(line.strip())