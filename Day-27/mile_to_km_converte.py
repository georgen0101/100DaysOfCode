from tkinter import *

# FONT = ("Arial", 24, "normal")

screen = Tk()
screen.title("Mile to Kilometer Converter")
screen.config(padx=20, pady=20)
# screen.minsize(width=500, height=300)

# Labels
label = Label(text="Miles")  # miles_label
label.grid(column=2, row=0)

label2 = Label(text="Kilometers")  # kilometer_label
label2.grid(column=2, row=1)

label3 = Label(text="is equal to")  # is_equal_label
label3.grid(column=0, row=1)

result = Label(text="0")  # kilometer_result_label
result.grid(column=1, row=1)

# Entry
entry = Entry(width=10)  # miles_input/entry
entry.insert(END, string="0")
entry.grid(column=1, row=0)


def button_action():  # miles_to_km
    miles = float(entry.get()) * 1.609
    result.config(text=round(miles, 4))


# Create a button
button = Button(text="Calculate", command=button_action)  # calculate_button
button.grid(column=1, row=2)


screen.mainloop()
