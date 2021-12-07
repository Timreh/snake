from turtle import Turtle


class Field:
    def __init__(self):
        self.field = self.create_field()

    def create_field(self):
        a = Turtle()
        a.hideturtle()
        a.color("red")
        a.pensize(4)
        a.up()
        a.goto(-302, -302)
        a.down()
        for i in range(4):
            a.forward(600)
            a.left(90)
