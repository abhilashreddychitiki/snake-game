import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()
snake = Snake()
food = Food()
game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #food collision detecting
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.set_score()
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment ==snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
