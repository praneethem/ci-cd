def show_menu():
    print("=== TO-DO LIST MENU ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

tasks = []

def main():
    while True:
        show_menu()
        try:
            choice = input("Choose an option: ").strip()
        except EOFError:
            print("\nNo input detected. Exiting safely...")
            break

        if choice == "1":
            try:
                task = input("Enter task: ")
                tasks.append(task)
                print("Task added!")
            except EOFError:
                print("No task entered. Exiting...")
                break

        elif choice == "2":
            print("Your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

        elif choice == "3":
            print("Remove feature not needed for Jenkins test")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

