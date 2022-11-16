from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make a bet", prompt="Which turtle will win the race?")
colors = ["red", "green", "orange", "blue", "yellow", "purple"]

y_coordinate = [0, -40, 40, -80, 80, 110]
all_turtles = []
for turtle_index in range(0, 6):
    # we create a new turtle everytime
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_coordinate[turtle_index])
    # append every turtle created to a list so that it can be accessed easily for the race
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    # we should get a way to move the turtles forward, I will append the turtles in the upper for loop to a new
    # list of turtles
    for turtle in all_turtles:
        if turtle.xcor() == 240:
            winner_color = turtle.pencolor()
            if user_guess == winner_color:
                print(f"You've won, {winner_color} is the winner.")
            else:
                print(f"You've lost, {winner_color} is the winner.")
            is_race_on = False

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
