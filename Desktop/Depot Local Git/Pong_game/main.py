import turtle
import winsound
from random import randint

window = turtle.Screen()
window.title("Pong game by @EssiJunior")
window.bgcolor("brown")
window.setup(width=900, height=600)
window.tracer(0)

colors = ["SpringGreen", "blue4", "DarkViolet", "Gold", "Aqua"]

# Paddle X
pad_x = turtle.Turtle()
pad_x.speed(0)
pad_x.shape("square")
pad_x.color("white")
pad_x.penup()
pad_x.shapesize(stretch_wid=6, stretch_len=0.5)
pad_x.goto(-420,0)
score_x = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1 
ball.dy = 1

# Paddle Y
pad_y = turtle.Turtle()
pad_y.speed(0)
pad_y.shape("square")
pad_y.color("white")
pad_y.shapesize(stretch_wid=6, stretch_len=0.5)
pad_y.penup()
pad_y.goto(420,0)
score_y = 0
#Score system
refery = turtle.Turtle()
refery.speed(0)
refery.color("white")
refery.penup()
refery.goto(0, 260)
refery.hideturtle()
refery.write("Player X: 0    Player Y: 0", align="center", font=("Courier", 24, "italic"))
# functions
def pad_x_up():
    y_cord = pad_x.ycor()
    if y_cord == 240:
        ...
    else:
        y_cord += 20
        pad_x.sety(y_cord)

def pad_x_down():
    y_cord = pad_x.ycor()
    if y_cord == -240:
        ...
    else:
        y_cord -= 20
        pad_x.sety(y_cord)

def pad_y_up():
    y_cord = pad_y.ycor()
    if y_cord == 240:
        ...
    else:
        y_cord += 20
        pad_y.sety(y_cord)

def pad_y_down():
    y_cord = pad_y.ycor()
    if y_cord == -240:
        ...
    else:
        y_cord -= 20
        pad_y.sety(y_cord)
# Actions
window.listen()
window.onkeypress(pad_x_up, "w")
window.onkeypress(pad_x_down, "z")
window.onkeypress(pad_y_up, "Up")
window.onkeypress(pad_y_down, "Down")
while True:
    window.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Ball path
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 440 :
        ball.goto(0, 0)
        ball.dx *= -1
        score_x += 1
        refery.clear()
        refery.write(f"Player X: {score_x}    Player Y: {score_y}", align="center", font=("Courier", 24, "italic"))
        if score_x%5 == 0:
            randvalue = randint(0,4)
            window.bgcolor(colors[randvalue])
    if ball.xcor() < -440 :
        ball.goto(0, 0)
        ball.dx *= -1
        score_y += 1
        refery.clear()
        refery.write(f"Player X: {score_x}    Player Y: {score_y}", align="center", font=("Courier", 24, "italic"))
        if score_y%5 == 0:
            randvalue = randint(0,4)
            window.bgcolor(colors[randvalue])
    # bouncing
    if (ball.xcor()>410 and ball.xcor() < 420) and (ball.ycor() < pad_y.ycor() + 60 and ball.ycor() > pad_y.ycor() - 60):
        ball.setx(400)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() < -410 and ball.xcor() > -420) and (ball.ycor() < pad_x.ycor() + 60 and ball.ycor() > pad_x.ycor() - 60):
        ball.setx(-400)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)