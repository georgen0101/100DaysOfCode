from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    return 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# if start_timer() == 1:
#     time_sec = 1500
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         time_format = '{:02d}:{:02d}'.format(mins, secs)
#         # print(time_format)
#         time.sleep(1)
#         time_sec -= 1


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 113, image=tomato_img)
canvas.create_text(100, 130, text="25:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

start_button = Button(text="Start", highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(text="✔", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


window.mainloop()
