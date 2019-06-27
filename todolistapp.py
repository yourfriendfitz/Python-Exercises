def menu():
  print("Enter 1 to Add a Task")
  print("Enter 2 to Delete a Task")
  print("Enter 3 to View your Tasks")
  print("Enter q to Quit this application")

choice = ""


todo = []

while choice != "q":
  menu()
  choice = input("Enter Here: ")
  if choice == "1":
    Add = input("What Task would you like to add? ") 
    Priority = input("What is the priority level of this task? High, Medium, or Low? ")
    todo.append({'title': Add,'priority': Priority})
    
#You want to keep the scope of one thing to do to one object. That one object represents all the information about that title. You don't want to mix the info, it's clumped together. 

  elif choice == "2":
    for i in range(0,len(todo),1):
      print(i,todo[i])
    deleteIndex = int(input("Enter Index Number of Task you want to delete "))
    todo.pop(deleteIndex)
    print(f"{deleteIndex} has been deleted from your list")
    
  elif choice == "3":
    for i in range(0,len(todo),1):
      print(i,todo[i])
    

  elif choice == "q":
    print("You have quit this application. Goodbye!")
    break