from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color: ")
colors = ["blue", "red", "orange", "yellow", "green", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.setposition(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
# when the user makes his bet, we start the race
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} color is the winner!")
            else:
                print(f"You've lost! The {winning_color} color is the winner!")
            is_race_on = False
        else:
            random_distance = randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
