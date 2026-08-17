#Functions that filter/sort data. These functions are used to process and manipulate data in various ways. Functions can take input parameters, perform operations on the data, and return the processed results. They can be used to filter data based on specific criteria, sort data in ascending or descending order, and perform other transformations as needed.

articles = [
    {"sku": "00000104", "name": "Farmers Reg Milk 2L", "price": 4.99},
    {"sku": "00000140", "name": "Oat Milk 2L", "price": 5.29},
    {"sku": "00000142", "name": "Almond Milk 2L", "price": 5.14}
]

def find_by_name(search_text):
    matches = []
    for item in articles:
        if search_text.lower() in item["name"].lower():
            matches.append(item)
    return matches

search_name = input("Enter product name to search: ")
results = find_by_name(search_name)

if len(results) == 0:
    print("No article found with that name")
elif len(results) == 1:
    item = results[0]
    print("Found:", item["name"], "- SKU:", item["sku"], "- $" + str(item["price"]))
else:
    print("Multiple matches found, please choose one:")
    for i in range(len(results)):
        print(i + 1, "-", results[i]["name"])
    
    choice = input("Enter the number of the correct item: ")
    choice = int(choice)
    selected = results[choice - 1]
    print("You selected:", selected["name"], "- SKU:", selected["sku"], "- $" + str(selected["price"]))