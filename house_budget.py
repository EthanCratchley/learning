from tkinter import *
import os
 
def register():
    global register_screen
    register_screen = Toplevel(window)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()

    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()

    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()

    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
# Designing window for login 
def login():
    global login_screen
    login_screen = Toplevel(window)
    login_screen.title("Login")
    login_screen.geometry("300x250")

    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()

    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
def register_user():
    username_info = username.get()
    password_info = password.get()
 
    # Check if the username already exists
    list_of_files = os.listdir()
    if username_info in list_of_files:
        user_already_exists()
        return  # Exit the function if the username is already taken
    
    # If the username is not taken, proceed with registration
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    # Clear the input fields
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    # Display a success message
    registration_success()

def login_verify():
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")

    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")

    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")

    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def user_already_exists():
    global exists_screen
    exists_screen = Toplevel(register_screen)
    exists_screen.title("Error")
    exists_screen.geometry("150x100")

    Label(exists_screen, text="Username already exists", fg="red").pack()
    Button(exists_screen, text="OK", command=delete_user_already_exists).pack()

def registration_success():
    global success_screen
    success_screen = Toplevel(register_screen)
    success_screen.title("Success")
    success_screen.geometry("150x100")

    Label(success_screen, text="Registration Success", fg="green").pack()
    Button(success_screen, text="OK", command=delete_registration_success).pack()

def home_analyze():
    global home_window
    home_window = Toplevel(window)
    home_window.title("Home Budget Analyzer")
    home_window.geometry("1000x1000")
    window.config(bg='grey')

    budget_options_label = Label(home_window, text="Home Budget Calculator", bg="blue", width="300", height="2", font=("Calibri", 20))
    budget_options_label.pack()

    calculate_button = Button(home_window, text="Calculate", height="2", width="30", command=calculate)
    calculate_button.pack()

    clear_button = Button(home_window, text="Reset", height="2", width="30", command=clear)
    clear_button.pack()

def calculate():
    ...

def clear():
    ...

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    home_analyze()

def delete_user_already_exists():
    exists_screen.destroy()

def delete_registration_success():
    success_screen.destroy()
    register_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

window = Tk()
window.title('Login or Register')
window.geometry('300x300')
window.config(bg='grey')

choice_label = Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13))
choice_label.pack()

login_button = Button(text="Login", height="2", width="30", command=login)
login_button.pack()

register_button = Button(text="Register", height="2", width="30", command=register)
register_button.pack()

window.mainloop()