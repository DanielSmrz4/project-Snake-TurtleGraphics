from turtle import Turtle, Screen

screen = Screen()
garry = Turtle("turtle")

def move_forward():
    garry.forward(20)

# Stisknutí klávesy
screen.listen()
screen.onkeypress(move_forward, "d")


screen.exitonclick()