from turtle import Screen
from paddle import Paddle
from ball import Ball
from dash import Dash
from scroreboard import ScoreBoard
import time

WIDTH_SCREEN = 800
HEIGHT_SCREEN = 600
LEFT_POSITION = (-360, 0)
RIGHT_POSITION = (360, 0)

# Set up main screen
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("Pong game - Two players")
my_screen.setup(WIDTH_SCREEN, HEIGHT_SCREEN)
my_screen.tracer(0)

# Create two paddle each side
left_paddle = Paddle(LEFT_POSITION)
right_paddle = Paddle(RIGHT_POSITION)

# Create ball
ball = Ball()
# Create scoreboard
scoreboard = ScoreBoard()
# Create dash separation
dash = Dash()
# Listen events
my_screen.listen()
my_screen.onkey(right_paddle.move_up, "Up")
my_screen.onkey(right_paddle.move_down, "Down")
my_screen.onkey(left_paddle.move_up, "w")
my_screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    # Detect out of bounds
    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.reset_position()

my_screen.exitonclick()
