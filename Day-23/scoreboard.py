from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("black")
        self.current_level = 1
        self.goto(x=-230, y=260)
        self.update_scoreboard()

    def level_up(self):
        self.current_level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)
