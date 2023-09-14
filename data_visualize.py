import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog  # Import the filedialog module
from tkinter import messagebox

# Initialize the dataframe to None
df = None

# Define functions for button actions
def open_action():
    global df  # Use the global dataframe
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if file_path:
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)  # Load the selected CSV file into the dataframe
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path, engine='openpyxl')  # Load the selected XLSX file into the dataframe
            else:
                messagebox.showerror("Error", "Unsupported file format")
                return

            # Display a pop-up message to indicate successful file upload
            messagebox.showinfo("Success", "File uploaded successfully.")
            # You can update your interface to display the data or provide other options here

            return df  # Return the loaded dataframe
        except Exception as e:
            messagebox.showerror("Error", f"Error loading file: {str(e)}")

    return None

def save_action():
    global df  # Use the global dataframe
    if df is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    df.to_csv(file_path, index=False)  # Save as CSV without the index
                elif file_path.endswith('.xlsx'):
                    df.to_excel(file_path, index=False, engine='openpyxl')  # Save as XLSX without the index
                # Display a pop-up message to indicate successful save
                messagebox.showinfo("Success", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {str(e)}")
    else:
        messagebox.showerror("Error", "No data to save.")

def array_action():
    global df  # Use the global dataframe
    if df is not None:
        array_window = Toplevel(window)
        array_window.title('Data Array')
        array_window.geometry('800x600')
        array_window.config(bg='grey')

        array_label = Label(array_window, 
                            text='Data Array:',
                            font=('Consolas', 20),
                            fg='black',
                            bg='grey')
        array_label.pack()

        # Create a scrollable text widget to display the data
        data_text = Text(array_window, wrap=NONE)
        data_text.pack(fill=BOTH, expand=YES)

        # Insert the DataFrame data into the text widget
        data_text.insert('1.0', df.to_string(index=False))

        # Create a vertical scrollbar for the text widget
        vsb = Scrollbar(array_window, orient="vertical", command=data_text.yview)
        vsb.pack(side="right", fill="y")
        data_text.configure(yscrollcommand=vsb.set)

    else:
        messagebox.showerror("Error", "No data to display. Please open a data file first.")

def charts_action():
    global df  # Use the global dataframe
    if df is not None:
        chart_window = Toplevel(window)
        chart_window.title('Charts')
        chart_window.geometry('800x600')
        chart_window.config(bg='grey')

        chart_label = Label(chart_window, 
                            text='Select a chart to display:',
                            font=('Consolas', 20),
                            fg='black',
                            bg='grey')
        chart_label.pack()

        # Line Chart Button
        line_chart_button = Button(chart_window, 
                                   height=3, 
                                   width=20, 
                                   text='Line Chart', 
                                   font=('Consolas', 15),
                                   command=lambda: line_chart('Close', 'Date', 'Close Price', 'Stock Price Over Time'))
        line_chart_button.pack()

        # Bar Chart Button
        bar_chart_button = Button(chart_window, 
                                   height=3, 
                                   width=20, 
                                   text='Bar Chart', 
                                   font=('Consolas', 15),
                                   command=lambda: bar_chart('Volume', 'Date', 'Volume', 'Volume Over Time'))
        bar_chart_button.pack()

        # Pie Chart Button
        pie_chart_button = Button(chart_window, 
                                   height=3, 
                                   width=20, 
                                   text='Pie Chart', 
                                   font=('Consolas', 15),
                                   command=lambda: pie_chart('Volume', 'Volume Composition'))
        pie_chart_button.pack()

        # Add more chart options and functions as needed

    else:
        messagebox.showerror("Error", "No data to chart. Please open a data file first.")

def bar_chart(data_column_name, x_label, y_label, title):
    global df  # Use the global dataframe
    # Select every 5th row
    df_every_5th = df.iloc[::5]
    if df is not None:
        if data_column_name in df.columns:
            plt.figure(figsize=(10, 6))
            plt.bar(df_every_5th['Date'], df_every_5th[data_column_name])
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.show()
        else:
            messagebox.showerror("Error", "Specified column not found in the dataframe.")
    else:
        messagebox.showerror("Error", "No data to chart. Please open a data file first.")

def pie_chart(data_column_name, title):
    global df  # Use the global dataframe
    # Select every 5th row
    df_every_5th = df.iloc[::5]
    if df is not None:
        if data_column_name in df.columns:
            data = df_every_5th[data_column_name].sum()
            df_pie = df_every_5th.groupby('Date')[data_column_name].sum().reset_index()
            labels = df_pie['Date']
            sizes = df_pie[data_column_name]
            plt.figure(figsize=(10, 6))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            plt.axis('equal')
            plt.title(title)
            plt.show()
        else:
            messagebox.showerror("Error", "Specified column not found in the dataframe.")
    else:
        messagebox.showerror("Error", "No data to chart. Please open a data file first.")


def line_chart(data_column_name, x_label, y_label, title):
    global df  # Use the global dataframe
    # Select every 10th row
    df_every_5th = df.iloc[::5]
    if df is not None:
        if data_column_name in df.columns:
            df_every_5th = df.iloc[::5]
            plt.figure(figsize=(10, 6))
            plt.plot(df_every_5th['Date'], df_every_5th[data_column_name])
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.show()
        else:
            messagebox.showerror("Error", "Specified column not found in the dataframe.")
    else:
        messagebox.showerror("Error", "No data to chart. Please open a data file first.")

def back_action():
    # Implement back actions
    # You can close the menu window or go back to the main window
    menu_window.destroy()

def menu_action():
    # Create a new window for the menu
    global menu_window
    menu_window = Toplevel(window)
    menu_window.title('Menu')
    menu_window.geometry('1000x1000')
    menu_window.config(bg='grey')

    back_button_widget = Button(menu_window, 
                        height=1, 
                        width=5, 
                        text='Back', 
                        font=('Consolas', 25),
                        command=back_action)  
    back_button_widget.pack(anchor='nw')

    # Add buttons or widgets specific to the menu window
    menu_label = Label(menu_window, 
                    text='Options:',
                    font=('Consolas', 40),
                    fg='black',
                    bg='grey')
    menu_label.pack()

    open_button_widget = Button(menu_window, 
                        height=3, 
                        width=20, 
                        text='Open Data', 
                        font=('Consolas', 25),
                        command=open_action)  
    open_button_widget.pack()

    charts_button_widget = Button(menu_window, 
                        height=3, 
                        width=20, 
                        text='Charts', 
                        font=('Consolas', 25),
                        command=charts_action)  
    charts_button_widget.pack()

    array_button_widget = Button(menu_window, 
                        height=3, 
                        width=20, 
                        text='Data Arrays and Sheets', 
                        font=('Consolas', 25),
                        command=array_action)  
    array_button_widget.pack() 

    save_button_widget = Button(menu_window, 
                        height=3, 
                        width=20, 
                        text='Save Data', 
                        font=('Consolas', 25),
                        command=save_action)  
    save_button_widget.pack()

# Create the main window
window = Tk()
window.title('Data Visualization Dashboard')
window.geometry('1000x1000')
window.config(bg='grey')

# Welcome Label
welcome_label = Label(window, 
                      text='Welcome to the Data Visualization Dashboard',
                      font=('Consolas', 40),
                      fg='black',
                      bg='grey')
welcome_label.pack()

# Menu Button
menu_button_widget = Button(window, 
                     height=3, 
                     width=20, 
                     text='Menu', 
                     font=('Consolas', 25),
                     command=menu_action)  # Assign the function to the button
menu_button_widget.pack()


# Start the main loop
window.mainloop()
