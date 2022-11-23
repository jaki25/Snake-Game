import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from ScoreBoard import Score
from bomb import Bomb
from bomb import segments
screen=Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
brojac=0
snake=Snake()
food=Food()
bomb=Bomb()

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
        score.incriseScore_decriseScore(brojac)
        score.writeScore()
        for i in range(0,brojac):
            bomb=Bomb()
        food.refresh()
    for bomb in segments:

        if snake.head.distance(bomb)<15:

            if brojac<1:
                game_is_on=False
                score.game_over()
            else:
                snake.cutSnake()
                brojac -= 1
                score.incriseScore_decriseScore(brojac)
                score.writeScore()
    if brojac%5==0:

        for i in segments[1:]:
            i.clearBomb()
        for i in range(1,len(segments)-1):
            segments.pop()

    #detect collision with the wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        game_is_on=False
        score.game_over()
# detect collision with snake tail
    for seg in snake.segments[1:]:

        if snake.head.distance(seg)<10:

                game_is_on=False
                score.game_over()

screen.exitonclick()
