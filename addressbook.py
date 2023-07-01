from tkinter import *

# --------------------------------------------------------

def submit_all():
    # Get the values from the entry fields
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    address_1 = address1_entry.get()
    address_2 = address2_entry.get()
    city_val = city_entry.get()
    province_val = province_entry.get()
    zipcode_val = zipcode_entry.get()
    home_phone = homephone_entry.get()
    mobile_phone = mobphone_entry.get()
    email_val = email_entry.get()
    birthday = bday_entry.get()

    # Open the file in append mode and write the information
    with open("address_book.txt", "a") as file:
        file.write("First Name: " + first_name + "\n")
        file.write("Last Name: " + last_name + "\n")
        file.write("Address 1: " + address_1 + "\n")
        file.write("Address 2: " + address_2 + "\n")
        file.write("City: " + city_val + "\n")
        file.write("Province: " + province_val + "\n")
        file.write("Zip Code: " + zipcode_val + "\n")
        file.write("Home Phone: " + home_phone + "\n")
        file.write("Mobile Phone: " + mobile_phone + "\n")
        file.write("Email: " + email_val + "\n")
        file.write("Birthday: " + birthday + "\n")
        file.write("\n")  

    # Clear the entry fields after submitting
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    address1_entry.delete(0, END)
    address2_entry.delete(0, END)
    city_entry.delete(0, END)
    province_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    homephone_entry.delete(0, END)
    mobphone_entry.delete(0, END)
    email_entry.delete(0, END)
    bday_entry.delete(0, END)

# --------------------------------------------------------

window = Tk()
window.title("Address Book")
window.geometry('350x400')
window.config()

# First Name
first_name_label = Label(window, text="First Name:")
first_name_label.place(x=3, y=5)
first_name_entry = Entry(window, bg='white', fg='black')
first_name_entry.pack()

# Last Name
last_name_label = Label(window, text="Last Name:")
last_name_label.place(x=3, y=30)
last_name_entry = Entry(window, bg='white', fg='black')
last_name_entry.pack()

# Address 1
address1_label = Label(window, text="Address 1:")
address1_label.place(x=3, y=58)
address1_entry = Entry(window, bg='white', fg='black')
address1_entry.pack()

# Address 2
address2_label = Label(window, text="Address 2:")
address2_label.place(x=3, y=88)
address2_entry = Entry(window, bg='white', fg='black')
address2_entry.pack()

# City
city_label = Label(window, text="City:")
city_label.place(x=3, y=115)
city_entry = Entry(window, bg='white', fg='black')
city_entry.pack()

# Province
province_label = Label(window, text="Province:")
province_label.place(x=3, y=141)
province_entry = Entry(window, bg='white', fg='black')
province_entry.pack()

# Zip Code
zipcode_label = Label(window, text="Zip Code:")
zipcode_label.place(x=3, y=170)
zipcode_entry = Entry(window, bg='white', fg='black')
zipcode_entry.pack()

# Home Phone
homephone_label = Label(window, text="Home #:")
homephone_label.place(x=0, y=200)
homephone_entry = Entry(window, bg='white', fg='black')
homephone_entry.pack()

# Mobile Phone
mobphone_label = Label(window, text="Mobile #:")
mobphone_label.place(x=0, y=230)
mobphone_entry = Entry(window, bg='white', fg='black')
mobphone_entry.pack()

# Email
email_label = Label(window, text="Email:")
email_label.place(x=3, y=260)
email_entry = Entry(window, bg='white', fg='black')
email_entry.pack()

# Birthday
bday_label = Label(window, text="Birthday:")
bday_label.place(x=3, y=290)
bday_entry = Entry(window, bg='white', fg='black')
bday_entry.pack()

# Submit Button
submitall_button = Button(window, text="Submit", command=submit_all)
submitall_button.place(x=195, y=315)

window.mainloop()
