#Allowing user to see inventory and enter an item to view its price.

dictionary = { 
    "Apple" : "$0.75", 
    "Bread" : "$0.88",
    "Milk" : "$3.50",
    "Muffins": "$2.75", 
    "Juice": "$1.50",
    "Cookies" : "$3.00"
}

print("Welcome to our store we have the following items!")
for i in dictionary:
    print(i)

user_input = input("Type one to see its price!:  ")
user_input = user_input.capitalize()

if user_input in dictionary:
    print(f"the price of {user_input} is " + dictionary[user_input])
else:
    print("We don't have that item, sorry.")



#This will allow the user to enter the first letter as either Upper or Lowercase. 
#This code will not return the correct value if the user enters the singular version of their item. 






