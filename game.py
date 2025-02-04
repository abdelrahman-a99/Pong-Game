import turtle
import time

# Initialize the game window
window = turtle.Screen()
window.title("Ping Pong")
window.setup(width=800, height=600)
window.bgcolor("black")
window.tracer(0)  # to stop the widow from updating automatically and update it manually

# Global variables
game_over_flag = False
start_time = time.time()
initial_speed = 0.2
speed_increase_interval = 5  # Increase speed every 5 seconds
speed_increase_factor = 0.02  # Speed increase factor
score1 = 0
score2 = 0
target_score = 5
game_mode = None  # Will be set to "single" or "multi" based on player choice
menu_text = None  # To store the start menu text

# Initialize paddles and ball
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
ball.dx = initial_speed
ball.dy = initial_speed

# Initialize score display
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)

# Function to draw game boundaries
def draw_line(start, end):
    line = turtle.Turtle()
    line.speed(0)
    line.color("white")
    line.penup()
    line.goto(start)
    line.pendown()
    line.goto(end)
    line.hideturtle()

# Draw game boundaries
draw_line((-400, 300), (400, 300))  # Top line
draw_line((-400, -300), (400, -300))  # Bottom line
draw_line((-400, 300), (-400, -300))  # Left line
draw_line((400, 300), (400, -300))  # Right line
draw_line((0, -300), (0, 300))  # Vertical middle line

# Function to display the start menu
def show_start_menu():
    global menu_text

    menu_text = turtle.Turtle()
    menu_text.speed(0)
    menu_text.color("white")
    menu_text.penup()
    menu_text.hideturtle()
    menu_text.goto(0, 100)
    menu_text.write("Ping Pong", align="center", font=("Arial", 50, "normal"))
    menu_text.goto(0, 0)
    menu_text.write("1. Single Player", align="center", font=("Arial", 30, "normal"))
    menu_text.goto(0, -50)
    menu_text.write("2. Multiplayer", align="center", font=("Arial", 30, "normal"))
    menu_text.goto(0, -150)
    menu_text.write("Press 1 or 2 to start", align="center", font=("Arial", 20, "normal"))

# Function to clear the start menu text
def clear_start_menu():
    global menu_text
    if menu_text:  # Check if menu_text exists
        menu_text.clear()  # Clear the start menu text
        menu_text = None  # Reset the menu_text variable

# Function to start the game in single-player mode
def start_single_player():
    global game_mode
    game_mode = "single"

    # window.clear()
    clear_start_menu()  # Clear the start menu text

    start_game()

# Function to start the game in multiplayer mode
def start_multiplayer():
    global game_mode
    game_mode = "multi"

    # window.clear()
    clear_start_menu()  # Clear the start menu text

    start_game()

# Function to initialize the game
def start_game():
    global start_time
    start_time = time.time()
    score.clear()
    score.write(f"Player1: {score1}                Player2: {score2}", align="center", font=(None, 20, "normal"))
    main_game_loop()

# Function to check for a winner
def check_winner():
    if score1 >= target_score or score2 >= target_score:
        if score1 > score2:
            winner = "Player 1"
        else:
            winner = "Player 2"
        game_over(winner)

# Function to handle game over
def game_over(winner):
    global game_over_flag
    game_over_flag = True

    ball.goto(0, 0)
    ball.dx = 0
    ball.dy = 0
    score.clear()
    score.goto(0, 50)
    score.write(f"   Game Over\n*{winner} wins!*", align="center", font=("Arial", 50, "normal"))
    score.goto(0, -50)
    score.write("Press Space to Play Again", align="center", font=("Arial", 20, "normal"))

# Function to reset the game
def reset_game():
    global score1, score2, game_over_flag, start_time
    game_over_flag = False

    score1 = 0
    score2 = 0
    ball.goto(0, 0)
    ball.dx = initial_speed
    ball.dy = initial_speed
    start_time = time.time()
    score.clear()
    score.goto(0, 250)
    score.write(f"Player1: {score1}                Player2: {score2}", align="center", font=(None, 20, "normal"))

# Player movement functions
def player1_up():
    y = player1.ycor()
    if y < 240:
        y += 20
        player1.sety(y)

def player1_down():
    y = player1.ycor()
    if y > -240:
        y -= 20
        player1.sety(y)

def player2_up():
    y = player2.ycor()
    if y < 240:
        y += 20
        player2.sety(y)

def player2_down():
    y = player2.ycor()
    if y > -240:
        y -= 20
        player2.sety(y)

# AI movement function
def ai_move():
    if game_mode == "single":  # Only move if in single-player mode
        if ball.dx > 0:  # Only move when the ball is moving towards the AI
            if ball.ycor() > player2.ycor() + 10:
                player2_up()
            elif ball.ycor() < player2.ycor() - 10:
                player2_down()

# Keyboard bindings
window.listen()
window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")
window.onkeypress(reset_game, "space")
window.onkeypress(start_single_player, "1")
window.onkeypress(start_multiplayer, "2")

# Main game loop
def main_game_loop():
    global score1, score2, game_over_flag, start_time
    while True:
        window.update()

        # AI movement
        ai_move()

        # Check the elapsed time and increase speed
        elapsed_time = time.time() - start_time
        if elapsed_time >= speed_increase_interval and not game_over_flag:
            ball.dx = round(ball.dx + speed_increase_factor * (1 if ball.dx > 0 else -1), 2)
            ball.dy = round(ball.dy + speed_increase_factor * (1 if ball.dy > 0 else -1), 2)
            start_time = time.time()

        # Ball movement logic
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Ball collision with top and bottom walls
        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.dy *= -1

        # Ball collision with left and right walls (scoring)
        if ball.xcor() >= 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            score.clear()
            score.write(f"Player1: {score1}                Player2: {score2}", align="center", font=(None, 20, "normal"))
            check_winner()

        if ball.xcor() <= -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            score.clear()
            score.write(f"Player1: {score1}                Player2: {score2}", align="center", font=(None, 20, "normal"))
            check_winner()

        # Ball collision with paddles
        if (ball.xcor() >= 340 and ball.xcor() <= 350) and (ball.ycor() <= player2.ycor() + 40 and ball.ycor() >= player2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() <= -340 and ball.xcor() >= -350) and (ball.ycor() <= player1.ycor() + 40 and ball.ycor() >= player1.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

# Show the start menu initially
show_start_menu()

# Start the main event loop
window.mainloop()
