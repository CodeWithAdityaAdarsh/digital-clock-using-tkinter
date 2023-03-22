from tkinter import *

import time

root = Tk()

root.title("Digital Clock")

# Set the size of the window

root.geometry("300x100")

# Define the font style

clock_font = ("Arial", 30, "bold")

# Create the label to display the time

clock_label = Label(root, font=clock_font, bg="black", fg="white")

# Function to update the clock

def update_clock():

    current_time = time.strftime("%H:%M:%S")

    clock_label.configure(text=current_time)

    clock_label.after(1000, update_clock)

# Pack the clock label into the window

clock_label.pack(fill=BOTH, expand=1)

# Call the update_clock function to start the clock

update_clock()

# Start the main event loop

root.mainloop()
