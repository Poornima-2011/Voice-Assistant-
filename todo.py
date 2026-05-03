# todo.py

todo_list = []

def add_task(task):
    """Add a new task to the to-do list."""
    todo_list.append(task)
    return f"Task '{task}' added to your to-do list."

def remove_task(task):
    """Remove a task from the to-do list."""
    if task in todo_list:
        todo_list.remove(task)
        return f"Task '{task}' removed from your to-do list."
    else:
        return "Task not found."

def show_tasks():
    """Show all tasks in the to-do list."""
    if todo_list:
        tasks = "\n".join([f"Task {i + 1}: {task}" for i, task in enumerate(todo_list)])
        return f"Here are your tasks:\n{tasks}"
    else:
        return "Your to-do list is empty."
