import turtle
import random

screen = turtle.Screen()
screen.title("Catch the Falling Objects")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

basket = turtle.Turtle()
basket.shape("square")
basket.color("black")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

score = 0
score_display = turtle.Turtle()
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

def move_left():
    x = basket.xcor()
    if x > -250:
        x -= 20
        basket.setx(x)

def move_right():
    x = basket.xcor()
    if x < 250:
        x += 20
        basket.setx(x)

screen.listen()
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

objects = []

def create_object():
    object = turtle.Turtle()
    object.shape("circle")
    object.color("red")
    object.shapesize(stretch_wid=1, stretch_len=1)
    object.penup()
    object.goto(random.randint(-280, 280), 250)
    objects.append(object)

def delete_object(object):
    object.hideturtle()
    objects.remove(object)

while score < 20:
    screen.update()

    for object in objects[:]:
        object.sety(object.ycor() - 2)

        if object.distance(basket) < 30:
            score += 1
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            delete_object(object)
        elif object.ycor() < -290:
            delete_object(object)

    if random.randint(1, 50) == 1:
        create_object()

score_display.clear()
score_display.write("Congratulations! You win!", align="center", font=("Courier", 24, "normal"))
turtle.done()
