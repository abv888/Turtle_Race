import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []

is_race_on = False

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=-25 * turtle_index)
    turtles_list.append(t)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
            is_race_on = False
        dist = random.randint(0, 10)
        turtle.forward(dist)

screen.exitonclick()
