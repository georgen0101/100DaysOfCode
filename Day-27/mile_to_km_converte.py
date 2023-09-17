from tkinter import *

# FONT = ("Arial", 24, "normal")

screen = Tk()
screen.title("Mile to Kilometer Converter")
screen.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles")  # miles_label

km_label = Label(text="Kilometers")  # kilometer_label

is_equal_label = Label(text="is equal to")  # is_equal_label

result_label = Label(text="0")  # kilometer_result_label

# Use the radio widget to convert miles to km and vice-versa.
# Radiobutton
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


entry = Entry(width=10)  # miles_input/entry
entry.insert(END, string="0")


def miles_to_km():  # miles_to_km
    miles = float(entry.get()) * 1.609
    result_label.config(text=round(miles, 4))


# Create a button
calculate_button = Button(text="Calculate", command=miles_to_km)  # calculate_button

# Grid
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
is_equal_label.grid(column=0, row=1)
result_label.grid(column=1, row=1)
entry.grid(column=1, row=0)
calculate_button.grid(column=1, row=2)


screen.mainloop()
