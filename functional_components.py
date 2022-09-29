# Import messagebox from tkinter
from tkinter import messagebox


# Create a function to run the app
def run(window, fields):
    # Create fields in the window
    fields(window, check)


# Create a function to check if data is valid or not
def check(data_list):
    if "" in data_list:
        messagebox.showwarning("Warning", "All values Required")
    else:
        report()


def report():
    pass
