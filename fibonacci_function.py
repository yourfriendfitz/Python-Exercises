#Create a function that allows a user to determine how many numbers a fibonacci sequence will go until. 

def Fibonnaci(n):
    a = 0
    b = 1
    i = 0
    fib = []
    while i < n:
        a,b = b, a + b
        fib.append(a)
        i = i + 1
    return fib

user_input = int(input("How many Fibonnaci numbers would you like to generate? "))

print(Fibonnaci(user_input))



