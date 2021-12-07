from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, 'normal')


class Score:
    def __init__(self) -> None:
        self.score = 0
        self.stt = self.score_turtle()

    def score_turtle(self):
        a = Turtle()
        a.up()
        a.hideturtle()
        a.goto(0, 310)
        a.write(f"Score: {self.score}", align="center",
                font='Arial')
        return a

    def add_score(self):
        self.score += 1
        self.stt.clear()
        self.stt.write(f"Score: {self.score}", align="center",
                       font='Arial')

    def end(self):
        self.stt.clear()
        self.stt.goto(0, 310)
        self.stt.write(f"  Game over .\nFinal score: {self.score}",
                       align="center", font="Arial")
