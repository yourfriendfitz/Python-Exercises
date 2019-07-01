#Take an array and make a new array of only the first and last elements. 
#This list ends exercise takes the users inputs and tells them their list ends. 

arr = []

arr2 = []

smallest = []

print("Hello! Enter 5 different numbers below and we will will you some fun things about them!")

for i in range(5):
    arr.append(int(input("Enter a different number here: ")))

#Make an addition function using a loop.

def addition(n):
    sum = 0
    for i in n:
        sum += i
    return sum

#Make a multiplication function using a loop. 

def multiply(n):
    m = 1
    for i in n:
        m *= i
    return m

#Make a smallest item function using a loop. 

def small(n):
    sm = n[0]
    for i in n:
        if i <= sm:
            sm = i
    return sm

#Make a largest item function using a loop. 

def large(n):
    lg = n[0]
    for i in n:
        if i >= lg:
            lg = i
    return lg

#Tell the user the first and last number then entered.  

print(arr[0], " is the first number in you entered and ", arr[-1], " is the last number you entered.")

sum_items = addition(arr)

print(f"The sum of your items equals {sum_items}!")

multiplication = multiply(arr)

print(f"All your numbers multiplied together are {multiplication}")

smallest_item = small(arr)

print(f"{smallest_item} is the smallest item you entered.")

largest = large(arr)

#Difference between the largest and smallest numbers

def difference(n):
    return largest - smallest_item
    

max_min = difference(arr)

print(f"{largest} is the largest item you entered")

print(f"{max_min} is the differnce between the largest and smallest numbers you entered.")










