# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks yet. Add some tasks to your list.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to update a task
def update_task(index, updated_task):
    if index >= 1 and index <= len(tasks):
        tasks[index - 1] = updated_task
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(index):
    if index >= 1 and index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task index.")

# Main menu
while True:
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        index = int(input("Enter the task number to update: "))
        updated_task = input("Enter the updated task: ")
        update_task(index, updated_task)
    elif choice == '4':
        view_tasks()
        index = int(input("Enter the task number to delete: "))
        delete_task(index)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
