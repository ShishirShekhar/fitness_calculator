# Import messagebox from tkinter
from tkinter import messagebox, Tk, Frame, Label


# Create a function to run the app
def run(window, fields):
    # Create fields in the window
    fields(window, check)


# Create a function to check if data is valid or not
def check(data_list):
    for data in data_list:
        if data.get() == "":
            messagebox.showwarning("Warning", "All values Required")
            break
    else:   
        report()


def report():
    # from tkinter import PhotoImage
    report_window = Tk()
    report_window.title('REPORT')
    report_window.geometry('400x600')

    report_frame = Frame(report_window)
    lab = Label(report_frame, text="Report", fg="white")
    lab.pack()

    report_frame.pack(fill='x')
