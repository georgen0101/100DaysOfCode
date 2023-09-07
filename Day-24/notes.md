# Day 24 - Files, Directories and Paths

What we made:
- Added the feature of higher score intro the snake game
- Learn about files

## Save the higher score when the game closes.
Changed the game_over message to a new method and now the snake returns to the center when it crashes.
```python


    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset()

    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # If the head collides with any segment in the tail
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()
```
Used Files knowledge to modify the class

```python
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
        with open("Modified-Snake-Game/data.txt", mode="r") as data:
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
            with open("Modified-Snake-Game/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        # Reset the score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

```

## About Files

### Open and read a file
```python
file = open("file.txt")  # Save the file object to a variable
contents = file.read()  # Read and save all the content of the file
print(contents)  # Prints the content of the file
```
The `open()` method has different types of modes to open a file.
- `r` Only read. (by default if the mode is not specified)
- `w` Only write. (Replace all the previous content)
- `a` Append, to add content.
- `r+` Only read and write.


### Write a file
```python
file = open("file.txt", mode="w")  
contents = file.write("New content")  # Rewrite all the previous content
print(contents)  # Will print 'New content'
```
- `write(str)` take strings as arguments.


### Append text
```python
file = open("file.txt", mode="a")
contents = file.write("+ Add this")  # Appends the string into the file.
print(contents)  # Will print 'New content + Add this'
```

## About Paths

```python
# Moved the new_file.txt to the desktop folder.

# Absolute Path
with open("/Users/laptop/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)


# Relative Path
with open("../../../Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)
```




