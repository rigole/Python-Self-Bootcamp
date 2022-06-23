from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))


# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
    
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)
   

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down") 

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

screen.listen()
#screen.onkey(go_up, "Up")
#screen.onkey(go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()