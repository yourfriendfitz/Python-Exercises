#Write another To Do List Applicatino that writes files to a JSON File

import json

def Menu():
    print("Enter 1 to Add a Task.")
    print("Enter 2 to Delete a Task.")
    print("Enter 3 to View Tasks.")
    print("Enter Q to Quit.")

todos = []

with open("todowrite.txt", "a+") as file_object:
    name = input("What's your name? ")
    file_object.write(name + "\n")
    choice = None
    while choice != "Q":
        Menu()
        choice = input(f"{name}, please choose from one of the above options: ")
        if choice == "1":
            add = input(f"What task would {name} like to add? ")
            priority = input("What is the priority level? High, Medium, or Low? ")

            todo = {
                "name": add,
                "priority": priority
            }
            todos.append(todo)
            with open ("todo1.json", "w") as file_object:
                json.dump(todos, file_object) 

        if choice == "2":
            for i in range(0, len(todos)):
                print(i, todos[i])
            delete = (input(f"What item would {name} like to delete? Or enter B to go back."))
            if delete == "B":
                Menu()
                choice = input(f"{name}, please choose from one of the above options: ")
            else:
                del todos[int(delete)]
                print(f"Here is {name}'s updated To Do List")
                for i in range(0, len(todos)):
                    print(i, todos[i])
    
        if choice == "3":
            print(f"Here are {name}'s' Todos!")
            for i in range(0, len(todos)):
                print(i, todos[i])
    print(f"{name} have quit the application. Goodbye!")



