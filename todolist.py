tasks = []
while True:
    print("----TO DO LIST----")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")
    choice = input("Enter your choice from (1-4): ")
    if choice == '1':
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    elif choice == '2':
        task = input("Enter the task you want to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed successfully.")
        elif len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print(f"Task '{task}' not found in the list.")
        

    elif choice == '3':
        if len(tasks)==0:
            print("No tasks in the list.")
        else:
            print("tasks in the list:")
            for i, task in enumerate(tasks, start=1):
             print(f"{i}. {task}")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
else:
    print("Invalid choice. Please enter a number between 1 and 4.")