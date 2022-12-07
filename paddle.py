from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, init_position):
        super().__init__()
        self.init_position = init_position
        self.create_paddle()

    def create_paddle(self):
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.goto(self.init_position)

    def move_up(self):
        if self.ycor() <= 230:
            new_ycor = self.ycor() + 20
            self.goto(self.init_position[0], new_ycor)

    def move_down(self):
        if self.ycor() >= -230:
            new_ycor = self.ycor() - 20
            self.goto(self.init_position[0], new_ycor)

    def reset_paddle(self):
        self.goto(self.init_position)





