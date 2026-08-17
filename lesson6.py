#Functions-reuse a piece of code. Basically functions are used to avoid writing the same code again and again. Functions are defined using the def keyword. The function name is followed by parentheses which may include parameters. The function body is indented and contains the code to be executed when the function is called. Functions can return values using the return statement.

articles=input("enter the SKU id: ")
padded_article=articles.zfill(16)
print("the padded article is:", padded_article)

#List of built in functions that can be used in code
#working with numbers:
#len(x) - returns the length of a string
#sum(list)-adds up all numbers ina  list
#max(list)/min(list)-biggest/smallest value return
#round(3.1459, 2)-rounds the number to 2 decimal places
#abs(-5)-absolute value removes negative number
#int(), float(), str()-converts to integer, float, string

#working with text:
#zfill(16)-pads the string with zeros to make it 16 characters long
#.upper()/.lower()-converts the string to uppercase/lowercase
#.strip()-removes extra spaces from start/end
#.replace("old", "new")-swap text
#.split(",")-splits the string into a list of substrings based on the delimiter
#.join(list)-joins a list of strings into a single string with the specified delimiter

#working with lists:
#.append(item)-adds an item to the end of the list
#.insert(index, item)-inserts an item at a specific index in the list
#.pop(index)-removes and returns the item at the specified index in the list
#.remove(item)-removes the first occurrence of the specified item from the list
#.sort()-sorts the list in ascending order
#.reverse()-reverses the order of the list
#sorted(list)-returns a new sorted list without modifying the original list
#list(range(1,10))-creates a list of numbers from 1 to 9

#Extra details:
#type(x)-returns the data type of x
#isinstance(x, type)-checks if x is an instance of the specified type
#in operator-checks if an item is in a list or string