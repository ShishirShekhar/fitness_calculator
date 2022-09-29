# Import all modules from tkinter
from tkinter import *

# Create window for the app
window = Tk()
# Add title of the window
window.title("Fitness Calculator")
# Add width and height of the window
window.geometry('390x844')

# Create the frame
frame1 = Frame(window, bg="black", height=6)
# Create a label
label1 = Label(frame1, text="", height=100, bg="black")
# Add/Pack the label in the frame
label1.pack()
# Fill the frame in x direction
frame1.pack(fill='x')

# Loop the window display
window.mainloop()
