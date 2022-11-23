from turtle import Turtle
import random
segments=[]
class Bomb(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
        segments.append(self)



    def refresh(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x, y)
