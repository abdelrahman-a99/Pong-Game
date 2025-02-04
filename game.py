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
score.write(f"Player1: {score1}                Player2: {score2}", align= "center", font=(None, 20, "normal"))

target_score = 5

def check_winner():
    if score1 >= target_score or score2 >= target_score:
        if score1 > score2:
            winner = "Player 1"
        else:
            winner = "Player 2"
        game_over(winner)

def game_over(winner):
    ball.goto(0, 0)
    ball.dx = 0
    ball.dy = 0
    score.clear()
    score.goto(0, 50)
    score.write(f"   Game Over\n*{winner} wins!*", align="center", font=("Arial", 50, "normal"))
    score.goto(0, -50)
    score.write("Press Space to Play Again", align="center", font=("Arial", 20, "normal"))

def reset_game():
    global score1, score2
    score1 = 0
    score2 = 0
    score.clear()
    score.goto(0, 250)
    score.write(f"Player1: {score1}                Player2: {score2}", align= "center", font=(None, 20, "normal"))
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2

def draw_line(start, end):
    line = turtle.Turtle()
    line.speed(0)
    line.color("white")
    line.penup()
    line.goto(start)
    line.pendown()
    line.goto(end)
    line.hideturtle()

def draw_center_circle(size, width=2):
    circle = turtle.Turtle()
    circle.speed(0)
    circle.color("white")
    circle.width(width)
    circle.penup()
    circle.goto(0, -(size))
    circle.pendown()
    circle.circle(size)
    circle.hideturtle()

def draw_center_dot(size):
    dot = turtle.Turtle()
    dot.speed(0)
    dot.color("white")
    dot.penup()
    dot.goto(0, 0)
    dot.pendown()
    dot.dot(size)
    dot.hideturtle()

draw_line((-400, 300), (400, 300))  # Top line
draw_line((-400, -300), (400, -300))  # Bottom line
draw_line((-400, 300), (-400, -300))  # Left line
draw_line((400, 300), (400, -300))  # Right line

draw_line((0, -300), (0, 300)) # vertical middle line

# draw_center_circle(100)
# draw_center_dot(10)

def player1_up():
    y = player1.ycor()
    if y < 240:  # Adjusted boundary to the top line
        y += 20
        player1.sety(y)

def player1_down():
    y = player1.ycor()
    if y > -240:  # Adjusted boundary to the bottom line
        y -= 20
        player1.sety(y)

def player2_up():
    y = player2.ycor()
    if y < 240:  # Adjusted boundary to the top line
        y += 20
        player2.sety(y)

def player2_down():
    y = player2.ycor()
    if y > -240:  # Adjusted boundary to the bottom line
        y -= 20
        player2.sety(y)

window.listen() # tell the window to expect keyboard input

window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")

window.onkeypress(reset_game, "space")  # Listen for the spacebar to reset the game

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
        score.write(f"Player1: {score1}                Player2: {score2}", align= "center", font=(None, 20, "normal"))
        check_winner()

    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player1: {score1}                Player2: {score2}", align= "center", font=(None, 20, "normal"))
        check_winner()

    if (ball.xcor() >= 340) and (ball.xcor() <= 350) and (ball.ycor() <= player2.ycor() + 40) and (ball.ycor() >= player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <= -340) and (ball.xcor() >= -350) and (ball.ycor() <= player1.ycor() + 40) and (ball.ycor() >= player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
