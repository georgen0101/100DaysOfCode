from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO 4: Save the entries into a txt file

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Don't leave empty fields")
    else:
        # Pop-up
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
                                                              f"\n Password: {password} \n Is it ok to save?")
        if is_ok:
            # Write the entries into the data file
            with open("./data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# TODO 1: Create the window
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# TODO 2: Create the canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)

# TODO 3: Create the labels and buttons
website_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")

website_entry = Entry(width=40)
website_entry.focus()  # Focus the cursor for the user to start typing
email_entry = Entry(width=40)
email_entry.insert(0, "example@gmail.com")
pass_entry = Entry(width=23)

generate_pass_button = Button(text="Generate Password", command=generate_password)
add_button = Button(width=37, text="Add", command=save)

# TODO 3.1: Make the grid layout
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
pass_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry.grid(column=1, row=3)

generate_pass_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
