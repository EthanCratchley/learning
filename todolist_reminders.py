from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pync
import time
from datetime import datetime

# Define a data structure to store task information, including reminders
tasks = []

# Function to delete a task
def delete_task():
    selected_task_index = listbox_task.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        listbox_task.delete(selected_task_index)
        del tasks[selected_task_index]

# Function to clear the task list
def clear_task_list():
    listbox_task.delete(0, END)
    tasks.clear()

# Function to mark a task as completed
def mark_completed():
    selected_task_index = listbox_task.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = tasks[task_index]
        task['completed'] = True
        listbox_task.itemconfig(task_index, {'fg': 'gray'})

# Function to save tasks to a file
def save_tasks():
    tasks_to_save = [task['description'] for task in tasks]
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("TXT Files", "*.txt")])

    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.writelines('\n'.join(tasks_to_save))
            messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {str(e)}")
    else:
        messagebox.showerror("Error", "No data to save.")

# Function to add a new task
def add_task():
    task_description = entry_task.get(1.0, "end-1c")
    reminder_enabled = reminder_var.get()
    reminder_datetime_str = reminder_time_var.get()

    if not task_description:
        messagebox.showwarning(title="Warning!", message="Please Enter Some Text!")
        return

    if reminder_enabled:
        # Validate the reminder date and time format
        try:
            reminder_datetime = datetime.strptime(reminder_datetime_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showwarning(title="Warning!", message="Invalid Date and Time Format!")
            return
    else:
        reminder_datetime = None

    tasks.append({
        'description': task_description,
        'reminder_enabled': reminder_enabled,
        'reminder_datetime': reminder_datetime,
        'completed': False  # Added 'completed' field
    })

    listbox_task.insert(END, task_description)
    entry_task.delete(1.0, END)
    reminder_time_var.set("")  # Clear the reminder time entry
    reminder_var.set(0)  # Uncheck the reminder checkbox

# Function to start reminders
def start_reminder():
    while True:
        current_datetime = datetime.now()
        for task in tasks:
            if task['reminder_enabled'] and task['reminder_datetime'] and current_datetime >= task['reminder_datetime']:
                pync.notify(title='To-Do Alert', message=task['description'])
                task['reminder_enabled'] = False  # Disable the reminder after it's triggered

        time.sleep(10)  # Sleep for 10 seconds

# Create the main window
window = Tk()
window.title("To-Do List with Reminders")
window.geometry('800x600')
window.config(bg='grey')

# Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

# Listbox to display tasks
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

# Scrollbar for the listbox
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Entry widget to add a new task
entry_task = Text(window, width=40, height=4)
entry_task.pack()

# Entry for setting reminder date and time
reminder_time_label = Label(window, text="Set Reminder Date and Time (YYYY-MM-DD HH:MM:SS):")
reminder_time_label.pack()
reminder_time_var = StringVar()
reminder_time_entry = Entry(window, textvariable=reminder_time_var)
reminder_time_entry.pack()

# Create a variable to store the state of the checkbox (1 for checked, 0 for unchecked)
reminder_var = IntVar()

# Checkbutton to enable reminders
reminder_checkbox = Checkbutton(window, text='Enable Reminder', variable=reminder_var, onvalue=1, offvalue=0)
reminder_checkbox.pack()

# Buttons to manage tasks
add_button = Button(window, text="Add Task", width=50, command=add_task)
add_button.pack(pady=3)

# Button to start reminders
start_button = Button(window, text="Start Reminders", width=50, command=start_reminder)
start_button.pack(pady=3)

delete_button = Button(window, text="Delete Selected Task", width=50, command=delete_task)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as Completed", width=50, command=mark_completed)
mark_button.pack(pady=3)

clear_button = Button(window, text="Clear List", width=50, command=clear_task_list)
clear_button.pack(pady=3)

save_button = Button(window, text="Save List", width=50, command=save_tasks)
save_button.pack(pady=3)

window.mainloop()
