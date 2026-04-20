'''
Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
    Add a task
    View all tasks
    Mark a task as completed
    Delete a task
    Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Example output:
Your Tasks:
1. Buy groceries || not_done
2. Finish Python project || done
3. Read a book || not_done

Bonus:
* Prevent empty tasks from being added.
* Validate task numbers before completing/deleting.
'''
import os
import sys
from datetime import datetime
 
def show_menu():
    print("*"*50)
    print("Terminal-Based Task List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("*"*50)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "done" if task["completed"] else "not done"
        print(f"{i}. {task['task']} || {status}")
    print("*"*50)

def mark_task_as_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']},{task['timestamp']}\n")
    print("Tasks saved to file.")

if __name__ == "__main__":
       tasks = []
       while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_as_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks_to_file(tasks)
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")