# Import all modules from tkinter
from tkinter import Tk, Frame, Label, Entry, IntVar, Radiobutton, Button, messagebox
# Import required function from report
from report import report

# Create a list to store input data
data_list = []
# Create a variable to store gender value
gender_value = 0
# Create a variable to store age
age_entry = 0


# Create a function to display home page
def home():
    # Create window for home page
    window = Tk()
    # Add title of the window
    window.title("Fitness Calculator")
    # Add width and height of the window
    window.geometry('500x600')
    
    # Add fields
    fields(window)
    
    # Loop the window display
    window.mainloop()


# Create a function to create different field
def fields(window):
    # Create name and age field
    name_age_field(window)
    
    # Create gender field
    gender_field(window)

    # Create health data entry field
    data_field(window)

    # Create a button to generate report
    generate = Button(window, text="Generate Report", command=check, height=2)
    generate.pack(pady=20)


# Create a function to create fields for name and age
def name_age_field(window):
    # Create a frame for name and age
    name_age_frame = Frame(window)
    name_age_frame.pack(pady=20)

    # Create name label
    name_label = Label(name_age_frame, text="Name:")
    name_label.grid(column=0, row=0)
    # Create a name entry
    name_entry = Entry(name_age_frame, bd=1)
    name_entry.grid(column=1, row=0, padx=5)

    # Create age label
    age_label = Label(name_age_frame, text="Age:")
    age_label.grid(column=3, row=0)
    # Create age entry
    global age_entry
    age_entry = Entry(name_age_frame, bd=1)
    age_entry.grid(column=4, row=0, padx=5)


# Create a function to create fields for gender
def gender_field(window):
    # Create a frame for gender
    gender_frame = Frame(window)
    gender_frame.pack()

    # Create label for gender
    gender_label = Label(gender_frame, text="Gender:")
    gender_label.grid(column=0, row=0)

    # Create a variable to store gender value using IntVar
    global gender_value
    gender_value = IntVar()

    # Create radio for male and female
    male_radio = Radiobutton(gender_frame, text="Male", variable=gender_value, value=0)
    male_radio.grid(column=1, row=0)
    female_radio = Radiobutton(gender_frame, text="Female", variable=gender_value, value=1)
    female_radio.grid(column=2, row=0)


# Create a function to create fields for health data
def data_field(window):
    # Create a frame for all health data values
    data_frame = Frame(window, pady=50)
    data_frame.pack()

    # Create a label for weight
    weight_label = Label(data_frame, text="Weight (Kgs):")
    weight_label.grid(column=0, row=0, sticky='w')
    # Create weight entry
    weight_entry = Entry(data_frame, bd=1)
    weight_entry.grid(column=1, row=0, sticky='e')
    # Add entry to the list
    data_list.append(weight_entry)

    # Create a label for height
    height_label = Label(data_frame, text="Height (Ms):")
    height_label.grid(column=0, row=1, sticky='w')
    # Create height entry
    height_entry = Entry(data_frame, bd=1)
    height_entry.grid(column=1, row=1, sticky='e')
    # Add entry to the list
    data_list.append(height_entry)

    # Create a label for BP Low
    bp_low_label = Label(data_frame, text="BP Low (mmHg):")
    bp_low_label.grid(column=0, row=2, sticky='w')
    # Create bp_low entry
    bp_low_entry = Entry(data_frame, bd=1)
    bp_low_entry.grid(column=1, row=2, sticky='e')
    # Add entry to the list
    data_list.append(bp_low_entry)

    # Create a label for BP High
    bp_high_label = Label(data_frame, text="BP High (mmHg):")
    bp_high_label.grid(column=0, row=3, sticky='w')
    # Create bp_high entry
    bp_high_entry = Entry(data_frame, bd=1)
    bp_high_entry.grid(column=1, row=3, sticky='e')
    # Add entry to the list
    data_list.append(bp_high_entry)

    # Create a label for Pulse Rate
    pulse_rate_label = Label(data_frame, text="Pulse Rate (bpm):")
    pulse_rate_label.grid(column=0, row=4, sticky='w')
    # Create Pulse Rate entry
    pulse_rate_entry = Entry(data_frame, bd=1)
    pulse_rate_entry.grid(column=1, row=4, sticky='e')
    # Add entry to the list
    data_list.append(pulse_rate_entry)

    # Create a label for RBC
    rbc_label = Label(data_frame, text="RBC (million/mm3):")
    rbc_label.grid(column=0, row=5, sticky='w')
    # Create RBC entry
    rbc_entry = Entry(data_frame, bd=1)
    rbc_entry.grid(column=1, row=5, sticky='e')
    # Add entry to the list
    data_list.append(rbc_entry)

    # Create a label for WBC
    wbc_label = Label(data_frame, text="WBC (cells/mm3):")
    wbc_label.grid(column=0, row=6, sticky='w')
    # Create WBC entry
    wbc_entry = Entry(data_frame, bd=1)
    wbc_entry.grid(column=1, row=6, sticky='e')
    # Add entry to the list
    data_list.append(wbc_entry)

    # Create a label for Platelets
    platelets_label = Label(data_frame, text="Platelets (billion/L):")
    platelets_label.grid(column=0, row=7, sticky='w')
    # Create Platelets entry
    platelets_entry = Entry(data_frame, bd=1)
    platelets_entry.grid(column=1, row=7, sticky='e')
    # Add entry to the list
    data_list.append(platelets_entry)

    # Create a label for HB
    hb_label = Label(data_frame, text="HB (g/dl):")
    hb_label.grid(column=0, row=8, sticky='w')
    # Create HB entry
    hb_entry = Entry(data_frame, bd=1)
    hb_entry.grid(column=1, row=8, sticky='e')
    # Add entry to the list
    data_list.append(hb_entry)

    # Create a label for Uric Acid
    uric_acid_label = Label(data_frame, text="Uric Acid (mg/dl):")
    uric_acid_label.grid(column=0, row=9, sticky='w')
    # Create Uric Acid entry
    uric_acid_entry = Entry(data_frame, bd=1)
    uric_acid_entry.grid(column=1, row=9, sticky='e')
    # Add entry to the list
    data_list.append(uric_acid_entry)

    # Create a label for Cholesterol
    cholesterol_label = Label(data_frame, text="Cholesterol (mg/dl):")
    cholesterol_label.grid(column=0, row=10, sticky='w')
    # Create Cholesterol entry
    cholesterol_entry = Entry(data_frame, bd=1)
    cholesterol_entry.grid(column=1, row=10, sticky='e')
    # Add entry to the list
    data_list.append(cholesterol_entry)


# Create a function to check if data is valid or not
def check():
    # Create a loop to check if the values are valid or not
    for data in data_list:
        # Show warning if value is empty
        if data.get() == "":
            messagebox.showwarning("Warning", "All values Required")
            break
    else:
        # Show report window
        report(data_list, gender_value, age_entry)
