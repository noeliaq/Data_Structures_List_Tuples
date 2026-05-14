#The list 

print ("=" *35)
print ("      My To-Do List")
print ("=" *35)
tasks = ["Walk the dog", "Grocery shopping", "Dance practice" ]

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
print (f"\nTotal tasks:{len(tasks)}")
print("\nWhat would you like to do ")
print ("1. Add a task")
print ("2. Remove a task")


#User options to add or remove 
try:
    choice = int(input("\nChoice: "))

    if choice == 1 :
         new_task = input("Enter a new task: ")
         tasks.append(new_task)
    
    elif choice == 2 :
        try:
             remove_tasks = (input ("Remove Tasks: "))
             index_number =tasks.index(remove_tasks)
             removed =tasks.pop(index_number)
        except ValueError:
                print (f"{remove_tasks} is not in the list ")
    else:
         print(f"{choice} is not valid option, enter number 1 or 2")
         print("program ending ")
         exit()
  #updating the list   
    print ("\nUpdated list:")
    for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    
    print (f"\nTotal tasks {len(tasks)}")
 
except ValueError:
    print ("Invalid, please enter number 1 or 2 ")
