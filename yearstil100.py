#This exercise is asking people their name and age, and printing out a message to them saying in what year they will turn 100. 

#ask user for their name.
chname = input("Hello! What's your name? ")

#ask user for their age. inputs are strings so we have to change it to an integer. 
chage = int(input(f"Hello {chname}! How old are you? "))

#give user an error if they do not put in an integer
# if chage > 100:
#     print("you did it wrong, and you know it. So Game Over!")

#take users age and subtract it from 100. 

years_until = 100 - chage


#print out final statement
print(f"Well {chname}, in {years_until} years you will turn 100 years old! Happy Early Birthday!")



