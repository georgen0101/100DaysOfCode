from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=260)
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        """Update the high score if the score is greater"""
        # Update the high_score
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        # Reset the score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
