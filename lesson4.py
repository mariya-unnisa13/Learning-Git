#Making Decisions with if/elif/else statements
age=int(input("Enter your age: "))
if age<0 or age>=120:
    print("Invalid age, please enter a valid age")
elif age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
