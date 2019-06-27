#Factorial project
x = int(input("Give me an Integer! "))

def factorial(n):
  f = 1
  for i in range (1, n+1):
    f = f * i
  return f

result = factorial(x)
print(f"The factorial of {x} is {result}")