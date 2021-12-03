from turtle import Turtle
from random import randint


class Food():
    def __init__(self, snake) -> None:
        self.snake = snake
        self.food = self.create_food()

    def create_food(self):
        a = Turtle()
        a.shapesize(0.2, 0.2)
        a.shape("square")
        a.color('blue')
        a.up()
        a.goto(self.food_pos())
        return a

    def food_pos(self):
        snake_pos = []
        for i in self.snake:
            snake_pos.append(i.pos())
        overlapping = True
        while overlapping:
            x = (randint(0, 150) - 75) * 4
            y = (randint(0, 150) - 75) * 4
            if (x, y) not in snake_pos:
                overlapping = False
        return x, y

    def eaten(self):
        self.food.goto(self.food_pos())
