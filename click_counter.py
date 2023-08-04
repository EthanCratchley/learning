from tkinter import *
import time

click_count = 0

def click_counter():
    global click_count
    click_count += 1
    display_clicks.delete(1.0, END)  # Clear the text box
    display_clicks.insert(1.0, f"Number of Clicks: {click_count}")

window = Tk()
window.title("Click Counter")
window.geometry("800x500")
window.config(bg="grey")

label_1 = Label(window, text="Click, CLick, CLIck, CLICk, CLICK, CLICK!", font=("Ink Free", 20))
label_1.pack()

display_clicks = Text(window, bg="black", fg="white", height=3, width=20)
display_clicks.pack()

click_button = Button(window, height=20, width=20, command=click_counter)
click_button.pack()

window.mainloop()
