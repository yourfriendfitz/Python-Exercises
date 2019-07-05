def Option():
    print("Enter [1] to convert Miles to Kilometers")
    print("Enter [2] to convert Kilometers to Miles")

def UserInput():
    choice = int(input("Make your selection: "))
    return choice



def Converter():
    Option()
    try:
        UserInput()
        if UserInput == 1:
            miles_calc = float(input("How many miles do you want to convert? "))
            km_distance = miles_calc * 1.60934
            print(f"{miles_calc} miles is ", round(km_distance,2), " kilometers.")
        elif UserInput == 2:
            kilo_calc = float(input("How many kilometers do you want to convert? "))
            mile_distance = kilo_calc / 1.60934
            print(f"{kilo_calc} kilometers is ", round(mile_distance, 2), " miles.")
        elif UserInput >= 3:
            print("There are only 2 options.")
        elif UserInput <= 1:
            print("You have to enter a positive number.")
    except ValueError:
        print("Enter a Valid option please!")
Converter()