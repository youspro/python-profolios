from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")

window.config(padx=30, pady=30)

def calculate():
    miles = miles_entry.get()
    km = float(miles) * 1.60934

    km = km
    km_number_label.config(text=km)


miles_entry = Entry(width=5)
miles_entry.get()
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_number_label = Label(text=0)
km_number_label.grid(column=1, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)




window.mainloop()