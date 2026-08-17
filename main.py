tasks = []

print("=== TO-DO LIST ===")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ").strip()

        if task:
            tasks.append({"task": task, "completed": False})
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            for index, item in enumerate(tasks, start=1):
                status = "✓ Completed" if item["completed"] else "○ Pending"
                print(f"{index}. {item['task']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            for index, item in enumerate(tasks, start=1):
                status = "✓ Completed" if item["completed"] else "○ Pending"
                print(f"{index}. {item['task']} - {status}")

            try:
                task_number = int(input("Enter task number to mark as complete: "))

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            for index, item in enumerate(tasks, start=1):
                status = "✓ Completed" if item["completed"] else "○ Pending"
                print(f"{index}. {item['task']} - {status}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Task '{deleted_task['task']}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
