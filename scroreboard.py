
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update()

    def increase_left_score(self):
        self.left_score += 1
        self.update()

    def increase_right_score(self):
        self.right_score += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.left_score, False, align=ALIGNMENT, font=FONT)
        self.goto(50, 200)
        self.write(self.right_score, False, align=ALIGNMENT, font=FONT)

