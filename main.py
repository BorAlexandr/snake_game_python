from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.show_score()

    '''Check detect collision with food'''
    if food.distance(snake.head) < 15:
        snake.extend_snake()
        food.refresh()
        scoreboard.current_score += 1

    '''Check detect collision with wall'''
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:

        if scoreboard.current_score > int(scoreboard.high_score):
            scoreboard.high_score = scoreboard.current_score
            scoreboard.record_hight_score(scoreboard.current_score)
        scoreboard.current_score = 0
        snake.refresh_snake()

    '''Check detect collision with snake segments'''
    for segment in snake.actual_snake[1:]:
        if snake.head.distance(segment) < 10:
            if scoreboard.current_score > int(scoreboard.high_score):
                scoreboard.high_score = scoreboard.current_score
                scoreboard.record_hight_score(scoreboard.current_score)
            scoreboard.current_score = 0
            snake.refresh_snake()




























screen.exitonclick()




























screen.exitonclick()
