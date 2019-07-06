name = input("Hello! What's your name? ")
task = input(f"And what do you want to yell at your kids {name}? " )
times = int(input(f"How many times to they need to hear to '{task}' before they actually do it? " ))
print("Here ya go!")


for i in range(times):
    print(task)