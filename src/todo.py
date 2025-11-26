todo_list = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit\n")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.append(task)
            print("Task added!")

        elif choice == "2":
            if not todo_list:
                print("No tasks yet.")
            else:
                for i, task in enumerate(todo_list):
                    print(f"{i+1}. {task}")

        elif choice == "3":
            if not todo_list:
                print("Nothing to remove.")
            else:
                index = int(input("Enter task number: ")) - 1
                if 0 <= index < len(todo_list):
                    removed = todo_list.pop(index)
                    print(f"Removed: {removed}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            

if __name__ == "__main__":
    main()

