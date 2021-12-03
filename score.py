from turtle import Turtle


class Score:
    def __init__(self) -> None:
        self.score = 0
        self.ST = self.score_turtle()

    def score_turtle(self):
        a = Turtle()
        a.up()
        a.hideturtle()
        a.goto(0, 250)
        a.write(f"Score: {self.score}")
