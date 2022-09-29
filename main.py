# Import all modules from tkinter
from tkinter import *
# Import the required functions from the functional_component
from functional_components import run
# Import the required functions from the display_functions
from display_functions import fields

# Create window for the app
window = Tk()
# Add title of the window
window.title("Fitness Calculator")
# Add width and height of the window
window.geometry('800x800')


# Run the app
run(window, fields)

# Loop the window display
window.mainloop()



