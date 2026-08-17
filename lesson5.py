#Loops-for and while

#for loops are sued when we know how many times to repeat or youre going through a list of items
for i in range(5):
    print("This is a simple loop", i)
#this give first 5 items

for i in range(1, 6):
    print("Read the number", i)

#this gives first five items belongs in the range of 1 to 5

#Lets learn list usage: collection of items stored in a single variable, separated by commas and enclosed in square brackets

cars=["BMW", "Chevy", "toyota", "Honda", "Ford", "Mazda"]
for car in cars:
    print("I like", car)

    #reads item in the list

#while loops are used for when we want to repeat the item until a certain condition is met.
traffic_light=["red", "yellow", "green"]
while traffic_light:
    light=traffic_light.pop(0)
    print("The traffic light is", light)