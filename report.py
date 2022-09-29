# Import messagebox from tkinter
from tkinter import messagebox, Tk, Frame, Label

# Create a function to check if data is valid or not
def check(data_list):
    # Create a loop to check if the values are valid or not
    for data in data_list:
        # Show warning if value is empty
        if data.get() == "":
            messagebox.showwarning("Warning", "All values Required")
            break
    else:
        # Show report window
        report()


# Create a function to display report page
def report():
    # Create window for report
    report_window = Tk()
    # Add title to the window
    report_window.title('REPORT')
    # Add width and height to the window
    report_window.geometry('400x600')

    # Create a frame to add title
    title_frame = Frame(report_window)
    # Add title label to the frame
    title = Label(title_frame, text="Report", fg="white")
    title.pack()

    # Pack title frame
    title_frame.pack(fill='x')
