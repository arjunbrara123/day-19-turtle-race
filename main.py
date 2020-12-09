from turtle import Turtle, Screen
import random

# Initial turtle graphic setup
screen = Screen()
screen.setup(width=500, height=400)
screen.delay(10)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour:").lower()
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# Place all turtles at the starting line
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.goto(x=-230, y=(40 * i - 100))
    new_turtle.clear()
    if user_bet == colours[i]:
        for j in range(31): new_turtle.shapesize((j % 3) + 1)
        new_turtle.stamp()
    else:
        new_turtle.penup()
    all_turtles.append(new_turtle)

# Start race
at_finish = False
headings = list(range(310, 410))
print(headings)
while not at_finish:
    for i in range(6):
        all_turtles[i].forward(random.randint(1, 10))
        all_turtles[i].setheading(random.choice(headings))
        if all_turtles[i].xcor() > 220:
            at_finish = True
            all_turtles[i].shapesize(2)
            winning_colour = all_turtles[i].pencolor()

print("The winning turtle was the " + str(winning_colour) + " turtle!")
if user_bet == winning_colour:
    print("Congrats! You win!")
else:
    print("Sorry, you didn't win this time!")

screen.exitonclick()
