from turtle import Turtle
import time

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVIN_DISTANCE=20

UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_Seg(position)


    def add_Seg(self, position):
        new_Seg = Turtle("square")
        new_Seg.color("white")
        new_Seg.penup()
        new_Seg.goto(position)
        self.segments.append(new_Seg)

    def extend(self):
        self.add_Seg(self.segments[-1].position())

    def move(self):

        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVIN_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)