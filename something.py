tasks = []

while True:
    print("To-Do List:")
    print("1.Add Task")
    print("2. View Tasks")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully.")
    elif choice == "2":
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please choose a valid option.")