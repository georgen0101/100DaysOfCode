# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     print(total)
#
#
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0)
# 55

### **kwargs
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)
# 25


# class Car:
#     def __init__(self, **kwargs):
#         self.color = kwargs.get("color")
#         #  The .get method returns the value of the keywords otherwise return None
#         self.model = kwargs.get("model")
#         self.make = kwargs.get("make")
#
#
# my_car = Car(color="White", model="Q5", make="Audi")



import tkinter

screen = tkinter.Tk()
screen.title("My first Tkinter program")
screen.minsize(width=500, height=300)

# Create a label
label = tkinter.Label(text="Hello, Tkinter!", font=("Arial", 25, "bold"))
label.grid(column=0, row=0)
# Add padding
label.config(padx=5, pady=5)

# Entry
u_input = tkinter.Entry()
u_input.grid(column=3, row=2)
# string_ex = u_input.get()
# print(string_ex)


def button_action():
    # label["text"] = "Button Got Clicked"
    # label.config(text="Button Got Clicked")  # "Makes more sense"
    label.config(text=u_input.get())


# Create a button
button = tkinter.Button(text="Click Me", command=button_action)
button.grid(column=1, row=1)

second_button = tkinter.Button(text="new Button")
second_button.grid(column=2, row=0)


screen.mainloop()
