from turtle import Turtle


class Snake:
    def __init__(self, size):
        self.size = size
        self.sss = self.create_snake()
        self.head = self.sss[0]

    def create_tt(self):
        a = Turtle()
        a.ht()
        a.shapesize(0.05*self.size, 0.05*self.size)
        a.shape("square")
        a.up()
        return a

    def create_snake(self):
        snake = []
        for i in range(5):
            tt = self.create_tt()
            tt.goto(self.size*(0-i), 0)
            tt.st()
            snake.append(tt)
        return snake

    def grow(self):
        newtt = self.create_tt()
        newtt.goto(self.sss[-1].pos())
        self.sss.append(newtt)
        newtt.st()
        # l1 = self.sss[-2]
        # l2 = self.sss[-3]
        # if l1.xcor() == l2.xcor():
        #     x = l1.xcor()
        #     if l1.ycor() > l2.ycor():  # 下行
        #         y = min(l1.ycor(), l2.ycor()) + \
        #             2 * (max(l1.ycor(), l2.ycor()) - min(l1.ycor(), l2.ycor()))
        #     else:  # 上行
        #         y = min(l1.ycor(), l2.ycor()) - \
        #             2 * (max(l1.ycor(), l2.ycor()) - min(l1.ycor(), l2.ycor()))
        # elif l1.ycor() == l2.ycor():
        #     y = l1.ycor()
        #     if l1.xcor() > l2.xcor():  # 左行
        #         x = min(l1.xcor(), l2.xcor()) + \
        #             2 * (max(l1.xcor(), l2.xcor()) - min(l1.xcor(), l2.xcor()))
        #     else:  # 右行
        #         x = min(l1.xcor(), l2.xcor()) - \
        #             2 * (max(l1.xcor(), l2.xcor()) - min(l1.xcor(), l2.xcor()))

    def collide(self):
        # 撞牆
        if self.head.xcor() > 300 or self.head.xcor() < -300 or \
                self.head.ycor() > 300 or self.head.ycor() < -300:
            return True
        # 自撞
        for i in range(1, len(self.sss)):
            if self.head.pos() == self.sss[i].pos():
                return True

    def move(self):
        for sge_num in range(len(self.sss)-1, 0, -1):
            self.sss[sge_num].goto(self.sss[sge_num - 1].position())
        self.head.forward(self.size)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
