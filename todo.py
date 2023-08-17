import time

# Store to do list
todo_list = []

# Start program
def main():
    print("Welcome to your To Do List!")
    time.sleep(1.5)
    options()

# Give options 
def options():
    while True:
        print("\nWhat would you like to do?")
        time.sleep(1)

        what_to_do = input("\nYour options are View List, Edit List, Save List, Load List, Quit: ").lower()

        if what_to_do == "view list":
            view_list()

        elif what_to_do == "edit list":
            edit_list()

        elif what_to_do == "save list":
            save_list()

        elif what_to_do == "load list":
            load_list()

        elif what_to_do == "quit":
            print("Goodbye!")
            exit()

        else:
            print("Please enter a valid input.")

# View to do list
def view_list():
    print("Here is your list:")
    for i, item in enumerate(todo_list, start=1):
        print(f"{i}. {item}")

# Edit to do list
def edit_list():
    print("Here is your list:")
    for i, item in enumerate(todo_list, start=1):
        print(f"{i}. {item}")

    edit_choice = input("\nWhat would you like to do? Add, Remove, Back: ").strip().lower()

    if edit_choice == "add":
        add()
    elif edit_choice == "remove":
        remove()
    elif edit_choice == " back":
        options()
    elif edit_choice == "quit":
        print("Goodbye!")
        exit()
    else:
        print("Please enter a valid input.")

# Add to list
def add():
    add_choice = input("What would you like to add?: ")
    todo_list.append(add_choice)
    print(f"The {add_choice} has been added to the list.")

# Remove from list
def remove():
    remove_choice = input("What would you like to remove?: ")
    if remove_choice in todo_list:
        todo_list.remove(remove_choice)
        print(f"The {remove_choice} has been removed from the list.")
    else:
        print("That is not on your list.")

# Save list
def save_list():
    custom_filename = input("Enter a custom file name (without extension): ")
    filename = f"{custom_filename}.txt"
    
    with open(filename, "w") as file:
        for item in todo_list:
            file.write(item + "\n")
    
    print(f"List saved successfully as '{filename}'.")

# Load List
def load_list():
    global todo_list
    custom_filename = input("Enter the name of the file to load (without extension): ")
    filename = f"{custom_filename}.txt"

    try:
        with open(filename, "r") as file:
            global todo_list
            todo_list = [line.strip() for line in file.readlines()]
        print(f"List loaded successfully from '{filename}'.")
    except FileNotFoundError:
        print("No saved list found.")

if __name__ == "__main__":
    main()
