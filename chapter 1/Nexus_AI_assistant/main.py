# store all tasks
tasks=[]

# main loop
while True:
    print("\n--- Nexus AI Assistant ---")
    print("1 . Add Task")
    print("2 . View Task")
    print("3 . Delete Task")
    print("4 . Update Tasks")
    print("5 . Save Tasks")
    print("6 . Exit")

    choice = input("Enter your Choice:")


    if choice == "1":
     task = input("Enter task: ")
     tasks.append(task)
     print("Task added Successfully")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available")

        else:

            for index, task in enumerate(tasks,start=1):
             print(index,task)

    elif choice == "3":
       
          delete_number=int(input("Enter task number to delete:"))
          tasks.pop(delete_number - 1)
          print("Task Deleted Successfully")

    elif choice == "4":
          
          update_number=int(input("Enter your task to be Updated:"))
          new_task=input("Enter new task:")
          tasks[update_number-1]=new_task
          print("Task Updated Successfully")
    
    elif choice == "5":

          file = open("tasks.txt", "w")

          for task in tasks:
              file.write(task + "\n")

          file.close()

          print("Tasks saved successfully")

    elif choice == "6":  
        break

    else:
        print("Invalid Choice")

