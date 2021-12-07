from turtle import Turtle
from random import randint


class Food():
    def __init__(self, snake, size) -> None:
        self.size = size
        self.snake = snake
        self.food = self.create_food()

    def create_food(self):
        a = Turtle()
        a.shapesize(0.05*self.size, 0.05*self.size)
        a.shape("circle")
        a.color('blue')
        a.up()
        a.goto(self.food_pos())
        return a

    def food_pos(self):
        food_range = 300 / self.size
        snake_pos = []
        for i in self.snake:
            snake_pos.append(i.pos())
        overlapping = True
        while overlapping:
            x = (randint(1, food_range - 1) - (food_range / 2)) * self.size
            y = (randint(1, food_range - 1) - (food_range / 2)) * self.size
            if (x, y) not in snake_pos:
                overlapping = False
        return x, y

    def eaten(self):
        self.food.goto(self.food_pos())
