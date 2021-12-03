import turtle
from turtle import Turtle, pensize
from snake import Snake
from food import Food
from score import Score
import time


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
timmy = Turtle()
timmy.goto(0, 250)
timmy.write("score:")


snake = Snake()
food = Food(snake.sss)
score = Score()
screen.listen()
while True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.pos() == food.food.pos():
        print("hoho")
        food.eaten()
        snake.grow()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
