from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
xcor = -230
ycor = -100
all_turtle = []

for turtle_index in range(0, 6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=xcor, y=ycor)
    all_turtle.append(new_turtle)
    ycor += 50
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner")
            else:
                print(f"You've lost! The {winning_color} turtle is winner")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
