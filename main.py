import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from ScoreBoard import Score
screen=Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
brojac=0
snake=Snake()
food=Food()

#text score
score=Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect collision with food
    if snake.head.distance(food)<15:
        brojac+=1
        snake.extend()
        score.incriseScore(brojac)
        score.writeScore()

        food.refresh()
#detect collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()
# detect collision with snake tail
    for seg in snake.segments:

        if seg== snake.head:
            pass
        elif snake.head.distance(seg)<10:

            game_is_on=False
            score.game_over()

screen.exitonclick()
