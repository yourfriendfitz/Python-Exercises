#Bouncer function to see who can get into the bar. 

def Bouncer():
    try:
        age = int(input("How old are you? "))
        if age < 18 and age > 0: 
            print("Sorry, you cannot enter.")
        elif age >= 18 and age < 21:
            print("You may enter but cannot consume alcohol.")
        elif age >=21 and age <=99 : 
            print("You may enter, please drink responsibly!")
        elif age <= 0:
            print("You cannot enter if you haven't been born yet.")
        elif age > 99:
            print("Wow! You're old! You may legally enter but please be careful!")
    except ValueError:
        print("Please enter a number.")
Bouncer()