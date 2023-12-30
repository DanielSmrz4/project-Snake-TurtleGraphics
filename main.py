from turtle import Turtle, Screen
import time
import random

# Proměnné
score = 0
highest_score = 0


screen = Screen()
screen.bgcolor("orange")
screen.title("Welcome to Snake")
screen.setup(width=600, height=600)
screen.tracer(False)

# Hlava hada
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"

# Potrava pro hada
food = Turtle("circle")
food.color("skyblue")
food.penup()
food.goto(100,100)

# Tělo hada
body_parts = []

# Skóre
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0,250)
score_sign.write("Skóre: 0 Nejvyšší skóre: 0", align='center', font=('Arial', 18))



# Funkce
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)    

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# Kliknutí na klávesy
screen.listen()
screen.onkeypress(move_up, "w")

screen.listen()
screen.onkeypress(move_down, "s")

screen.listen()
screen.onkeypress(move_left, "a")

screen.listen()
screen.onkeypress(move_right, "d")


# Hlavní cyklus
while True:
    screen.update()

    # Kolize s hranou plátna
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1.5)
        head.goto(0,0)
        head.direction = "stop"

        # Skryjeme části těla
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)

        # Vyprázdníme list s částmi těla
        body_parts.clear()

        # Resetování skóre
        score = 0

        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align='center', font=('Arial', 18))

    # Had sní jídlo
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y) 

        # Přidání části těla
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

        # Zvýšení skóre
        score += 10

        if score > highest_score:
            highest_score = score

        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align='center', font=('Arial', 18))    

    # První dílek těla následuje hlavu
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)

    # Další a další dílek následuje ten před sebou
    for index in range(len(body_parts) - 1, 0, -1):
        x = body_parts[index - 1].xcor()    
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x,y)


    move()

    # Kolize hlavy s tělem
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(1.5)
            head.goto(0,0)
            head.direction == "stop"
            
            # Skryjeme části těla
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)

            # Vyprázdníme list s částmi těla
            body_parts.clear()

            # Resetování skóre
            score = 0

            score_sign.clear()
            score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align='center', font=('Arial', 18))


    time.sleep(0.1)
    



screen.exitonclick()
