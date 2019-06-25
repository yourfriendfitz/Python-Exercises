check = input("How much was the bill? ")

tip = input("What percentage do you want to tip? (ex: .15) ")

tip_calc = float(check) * float(tip)

total = round(float(check) + (float(check) * float(tip)),2)

print(f"The amount you're tipping is ${tip_calc}, and the total you are paying for this service is ${total}.")

#Seperate Calculator that allows user to enter tip as a number. 

check2 = input("How much was the bill? ")

tip2 = input("What percentage do you want to tip? (ex: 15) ")

tip_calc2 = float(check2) * (float(tip2)/100)

total2 = round(float(check2) + (float(check2) * float(tip2)/100),2)

print(f"The amount you're tipping is ${tip_calc2}, and the total you are paying for this service is ${total2}.")