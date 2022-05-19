from turtle import Turtle, Screen
import random
import turtle

tim = Turtle() 
screen  = Screen()
turtle.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r,b,g)
    return random_color

for _ in range(40):
    tim.color(random_color())
    tim.circle(80)
    tim.left(10)

tim.hideturtle()

screen.exitonclick()
