import turtle
from turtle import Turtle, pensize
from record import Records
from snake import Snake
from food import Food
from score import Score
from field import Field
import time
# **********
# Todo"
# 1. bug:   File "c:\Users\Timreh\python\learning\hundred_day\d20_21\snake.py", line 46, in grow
# newtt.goto(x, y)
# UnboundLocalError: local variable 'x' referenced before assignment
# size 1, speed 5會出現
# 2. 記分板 (可能要用pandas)
# 3. 輸入紀錄
# 4. 不要創造個體(用self去寫就好)
# **********


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=700, height=700)
    screen.title("Snake Game")
    screen.tracer(0)

    SPEED = int(screen.textinput(
        title="Speed", prompt="Enter the speed of your snake(1~10): "))
    SPEED = 0.11 - (SPEED * 0.01)

    SIZE = int(screen.textinput(
        title="Snake Size", prompt="Enter the size of your snake(1~5): "))

    Field()
    screen.update()
    snake = Snake(SIZE)
    food = Food(snake.sss, SIZE)
    score = Score()
    screen.listen()

    while True:
        screen.update()
        time.sleep(SPEED)
        snake.move()

        if snake.collide():
            break

        if round(snake.head.xcor()) == round(food.food.xcor()) and \
                round(snake.head.ycor()) == round(food.food.ycor()):
            print("hoho")
            food.eaten()
            snake.grow()
            score.add_score()
        screen.onkey(key="Up", fun=snake.up)
        screen.onkey(key="Down", fun=snake.down)
        screen.onkey(key="Left", fun=snake.left)
        screen.onkey(key="Right", fun=snake.right)

    score.end()
    Records(SIZE, score.score).exec()

    screen.exitonclick()
