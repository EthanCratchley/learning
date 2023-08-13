import os
from tkinter import *

def submit_notes():
    # Get the text from the notes_text widget
    notes = notes_text.get("1.0", END).strip()  # Remove the trailing newline
    try: 
        if notes:  # Check if there's non-empty text before writing
                    # Specify the folder path where the notes will be saved
            folder_path = "notes"

            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Get the desired file name from the user
            file_name = file_name_entry.get()

            # Open the file in append mode and write the information
            file_path = os.path.join(folder_path, file_name)
            # Open the file in append mode and write the information
            with open(file_path, "a") as file:
                file.write(notes + "\n")  # Add a newline after writing

            # Clear the text after submitting
            notes_text.delete("1.0", END)
            file_name_entry.delete(0, END)
    except (ValueError, NameError, TypeError):
        print("Error.")

window = Tk()  
window.title("Notes Blank Slate")
window.geometry('500x525')

# Notes Text Box
notes_text = Text(window, bg='white', fg='black', width=60, height=35)
notes_text.pack()

# File Name Entry
file_name_label = Label(window, text="File Name:")
file_name_label.pack()
file_name_entry = Entry(window, width=30)
file_name_entry.pack()

# Submit Button
submit_n_button = Button(window, text="Submit", command=submit_notes)
submit_n_button.place(x=410, y=465)

window.mainloop()
