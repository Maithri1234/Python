class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("Your To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    todo_app = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo_app.add_task(task)
        elif choice == "2":
            todo_app.display_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
