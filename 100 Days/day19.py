from turtle import Turtle, Screen, color
import random

screen = Screen()
screen.setup(width = 500, height = 400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [150, 100, 50, 0, -50, -100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You lose. The {winning_turtle} turtle was the winner.")
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
