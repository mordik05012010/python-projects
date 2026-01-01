def to_do_list():
    tasks = []

    while True:
        print("\nMenu:" \
        "\n1.Show tasks." \
        "\n2.Add a task." \
        "\n3.Delete a task." \
        "\n4.Exit." \
        "\nYou choose: ")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if tasks:
                print("Your tasks: ")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks are there.")

        elif choice == "2":
            task = input("Enter a task: ").strip()
            if task == "":
                print("You didnt write anything")
            else:
                tasks.append(task)
                print(f"'{task}' has been successfully added to the list.")

        elif choice == "3":
            try:
                removed_task = int(input("Enter the task number you want to remove: "))
            except ValueError:
                print("You have to write an integer")
            else:
                if 0 < removed_task <= len(tasks):
                    tasks.pop(removed_task - 1)
                    print(f"The task was successfully removed.")
                else:
                    print("Invalid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")
             
to_do_list()
