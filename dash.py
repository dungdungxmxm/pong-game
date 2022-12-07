from turtle import Turtle

class Dash(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.create_dash()

    def create_dash(self):
        self.setheading(270)
        while self.ycor() >= -220:
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)