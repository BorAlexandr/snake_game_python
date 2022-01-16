from turtle import Turtle


class Snake:
    START_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.actual_snake = []
        self.make_start_snake()
        self.head = self.actual_snake[0]

    def make_start_snake(self):
        for coordinates in self.START_COORDINATES:
            self.add_snake_segment(coordinates)


    def add_snake_segment(self, position):
        coordinates_x, coordinates_y = position[0], position[1]
        start_snake = Turtle("square")
        start_snake.penup()
        start_snake.color("white")
        start_snake.goto(coordinates_x, coordinates_y)
        self.actual_snake.append(start_snake)


    def extend_snake(self):
        self.add_snake_segment(self.actual_snake[-1].position())


    def move(self):
        for index_segment in range(len(self.actual_snake) - 1, 0, -1):
            next_x = self.actual_snake[index_segment - 1].xcor()
            next_y = self.actual_snake[index_segment - 1].ycor()
            self.actual_snake[index_segment].goto(next_x, next_y)
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def position_head_snake(self):
        return self.head.pos()

