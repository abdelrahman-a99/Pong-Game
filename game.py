import turtle

window = turtle.Screen()
window.title("Ping Pong")
window.setup(width=800, height=600)
window.bgcolor("black")
window.tracer(0)  # to stop the widow from updating automatically and update it manually

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup() # stop the object from drawing lines
player1.goto(-350, 0)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup() # stop the object from drawing lines
player2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup() # stop the object from drawing lines
ball.goto(0, 0)

ball.dx = 0.2
ball.dy = 0.2

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write(f"Player 1: {score1} Vs Player 2: {score2}", align= "center", font=(None, 20, "normal"))

def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

window.listen() # tell the window to expect keyboard input

window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1} Vs Player 2: {score2}", align= "center", font=(None, 20, "normal"))

    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1: {score1} Vs Player 2: {score2}", align= "center", font=(None, 20, "normal"))

    if (ball.xcor() >= 340) and (ball.xcor() <= 350) and (ball.ycor() <= player2.ycor() + 40) and (ball.ycor() >= player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <= -340) and (ball.xcor() >= -350) and (ball.ycor() <= player1.ycor() + 40) and (ball.ycor() >= player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
