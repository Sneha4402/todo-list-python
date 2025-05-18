import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(todo_list, file, indent=4)

todo_list = load_tasks()


def add_task():
    task = input("Enter the task: ")
    todo_list.append({"title": task, "done": False})
    save_tasks()
    print("✅ Task Added Successfully!")

def view_tasks():
    if len(todo_list) == 0:
        print("🟡 No tasks yet.")
        return
    print("\n📝 Your Tasks:")
    for i, task in enumerate(todo_list, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) -1
        if 0<=index < len(todo_list):
            removed = todo_list.pop(index)
            save_tasks()
            print(f"🗑️ Deleted: {removed['title']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) -1
        if 0<=index < len(todo_list):
            todo_list[index]["done"] = True
            save_tasks()
            print("✅ Task marked as done.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a New Task")
        print("2. View all Tasks")
        print("3. Remove a Task")
        print("4.Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your option (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            save_tasks()
            print("💾 Tasks saved. Exiting the program.")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    menu()