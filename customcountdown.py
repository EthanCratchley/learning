from tkinter import *
from tkinter import colorchooser, font
import time
import datetime

# Global variables for customization
customization_options = {
    "background_color": "limegreen",
    "text_color": "black",
}

# Function to open color picker and update background color
def choose_c_background_color():
    color = colorchooser.askcolor()[1]
    if color:
        customization_options["background_color"] = color
        clock_label.config(bg=color)

# Function to open color picker and update background color
def choose_w_background_color():
    color = colorchooser.askcolor()[1]
    if color:
        customization_options["background_color"] = color
        window.config(bg=color)

# Function to open color picker and update background color
def choose_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        customization_options["text_color"] = color
        clock_label.config(fg=color)

# Function to update the clock label with the current time
def update_clock_label():
    # Calculate the time remaining until January 1, 2024
    target_date = datetime.datetime(2024, 1, 1)
    current_time = datetime.datetime.now()
    time_difference = target_date - current_time

    # Calculate the total seconds remaining
    total_seconds = time_difference.total_seconds()

    # Calculate the fractional time as a decimal (seconds / total seconds in a day)
    fractional_time = total_seconds / (24 * 60 * 60)

    # Create a composite string with the main text and subtext
    main_text = f"{fractional_time:.6f}"
    subtext = "days until 2024"
    composite_text = f"{main_text}\n{subtext}"

    # Update the clock label with the composite text
    clock_label.config(text=composite_text)

    window.after(1000, update_clock_label)  # Update every second

# Allow Clock Movement
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

# Allow Clock Movement
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

# Customize Clock Settings
def customize_clock():
    customize_window = Toplevel(window)
    customize_window.title("Customize Clock")

    # Clock Background color customization
    background_c_color_button = Button(customize_window, text="Clock Background Color", command=choose_c_background_color)
    background_c_color_button.pack()

    # Window Background color customization
    background_w_color_button = Button(customize_window, text="Window Background Color", command=choose_w_background_color)
    background_w_color_button.pack()

    # Text Color Customization
    text_color_button = Button(customize_window, text="Text Color", command=choose_text_color)
    text_color_button.pack()


window = Tk()
window.title('Custom Countdown Clock')
window.geometry('500x500')
window.config(bg=customization_options["background_color"])

customize_button = Button(window, 
                        height=2, 
                        width=6, 
                        text='Customize', 
                        font=('Consolas', 15), 
                        bg=customization_options["background_color"],
                        fg=customization_options.get("text_color", "black"),  # You can set a default color like "black"
                        command=customize_clock,)
customize_button.pack(anchor='nw')

clock_label = Label(window, 
                    text='',
                    font=('Consolas', 40),
                    fg='black',
                    bg="limegreen")
clock_label.pack()

clock_label.bind("<Button-1>", drag_start)
clock_label.bind("<B1-Motion>", drag_motion)

# Start updating the clock label
update_clock_label()

window.mainloop()
