import turtle
import time

# Initialize the game window
window = turtle.Screen()
window.title("Ping Pong")
window.setup(width=800, height=600)
window.bgcolor("black")
window.tracer(0)

# Global variables
game_over_flag = False
start_time = time.time()
initial_speed = 0.2
speed_increase_interval = 5
speed_increase_factor = 0.02
score1 = 0
score2 = 0
target_score = 5
game_mode = None
menu_text = None
difficulty_text = None
customization_text = None
difficulty = "medium"
paused = False
countdown_text = None

# Customization options
paddle_colors = ["blue", "red", "green", "yellow", "purple", "orange"]
ball_colors = ["white", "red", "blue", "green", "yellow", "purple"]
background_colors = ["black", "gray", "lightblue", "lightgreen", "lightyellow", "pink"]
game_speeds = ["slow", "normal", "fast"]

# Initialize paddles and ball
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
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
    menu_text.goto(0, -100)
    menu_text.write("3. Customization", align="center", font=("Arial", 30, "normal"))
    menu_text.goto(0, -150)
    menu_text.write("Press 1, 2, or 3 to start", align="center", font=("Arial", 20, "normal"))

    # Reset main menu key bindings
    reset_main_menu_keys()

# Function to clear the start menu text
def clear_start_menu():
    global menu_text
    if menu_text:
        menu_text.clear()
        menu_text = None

# Function to start the game in single-player mode
def start_single_player():
    global game_mode
    game_mode = "single"

    clear_start_menu()

    show_difficulty_menu()
    bind_difficulty_keys()

# Function to start the game in multiplayer mode
def start_multiplayer():
    global game_mode
    game_mode = "multi"

    clear_start_menu()

    start_game()

# Function to show difficulty menu
def show_difficulty_menu():
    global difficulty_text

    difficulty_text = turtle.Turtle()
    difficulty_text.speed(0)
    difficulty_text.color("white")
    difficulty_text.penup()
    difficulty_text.hideturtle()
    difficulty_text.goto(0, 100)
    difficulty_text.write("Select Difficulty", align="center", font=("Arial", 30, "normal"))
    difficulty_text.goto(0, 0)
    difficulty_text.write("1. Easy", align="center", font=("Arial", 20, "normal"))
    difficulty_text.goto(0, -50)
    difficulty_text.write("2. Medium", align="center", font=("Arial", 20, "normal"))
    difficulty_text.goto(0, -100)
    difficulty_text.write("3. Hard", align="center", font=("Arial", 20, "normal"))
    difficulty_text.goto(0, -200)
    difficulty_text.write("Press 1, 2, or 3 to select", align="center", font=("Arial", 15, "normal"))

# Function to set difficulty level
def set_difficulty(level):
    global difficulty, initial_speed, speed_increase_factor

    difficulty = level

    if difficulty == "easy":
        initial_speed = 0.15
        speed_increase_factor = 0.01

    elif difficulty == "medium":
        initial_speed = 0.2
        speed_increase_factor = 0.02

    elif difficulty == "hard":
        initial_speed = 0.25
        speed_increase_factor = 0.03

    clear_difficulty_menu()

    start_game()

# Function to clear the difficulty menu text
def clear_difficulty_menu():
    global difficulty_text
    if difficulty_text:
        difficulty_text.clear()
        difficulty_text = None

# Function to show customization menu
def show_customization_menu():
    global customization_text

    clear_start_menu()

    customization_text = turtle.Turtle()
    customization_text.speed(0)
    customization_text.color("white")
    customization_text.penup()
    customization_text.hideturtle()
    customization_text.goto(0, 100)
    customization_text.write("Customization", align="center", font=("Arial", 30, "normal"))
    customization_text.goto(0, 0)
    customization_text.write("1. Paddle Color", align="center", font=("Arial", 20, "normal"))
    customization_text.goto(0, -50)
    customization_text.write("2. Ball Color", align="center", font=("Arial", 20, "normal"))
    customization_text.goto(0, -100)
    customization_text.write("3. Background Color", align="center", font=("Arial", 20, "normal"))
    customization_text.goto(0, -150)
    customization_text.write("4. Game Speed", align="center", font=("Arial", 20, "normal"))
    customization_text.goto(0, -200)
    customization_text.write("Press 1, 2, 3, or 4 to select", align="center", font=("Arial", 15, "normal"))

    # Bind customization keys
    bind_customization_keys()

# Function to clear the customization menu text
def clear_customization_menu():
    global customization_text
    if customization_text:
        customization_text.clear()
        customization_text = None

# Function to set paddle color
def set_paddle_color(color):
    player1.color(color)
    player2.color(color)

# Function to set ball color
def set_ball_color(color):
    ball.color(color)

# Function to set background color
def set_background_color(color):
    window.bgcolor(color)

# Function to set game speed
def set_game_speed(speed):
    global initial_speed

    if speed == "slow":
        initial_speed = 0.1
    elif speed == "normal":
        initial_speed = 0.2
    elif speed == "fast":
        initial_speed = 0.3

    clear_customization_menu()
    show_start_menu()  # Return to the start menu after setting the speed

# Function to handle customization options
def handle_customization(option):
    clear_customization_menu()

    if option == 1:  # Paddle color
        show_color_menu("paddle")
    elif option == 2:  # Ball color
        show_color_menu("ball")
    elif option == 3:  # Background color
        show_color_menu("background")
    elif option == 4:  # Game speed
        show_speed_menu()

# Function to show color menu
def show_color_menu(item):
    global customization_text

    customization_text = turtle.Turtle()
    customization_text.speed(0)
    customization_text.color("white")
    customization_text.penup()
    customization_text.hideturtle()
    customization_text.goto(0, 100)
    customization_text.write(f"Select {item.capitalize()} Color", align="center", font=("Arial", 30, "normal"))

    y = 0
    for i, color in enumerate(paddle_colors if item == "paddle" else ball_colors if item == "ball" else background_colors):
        customization_text.goto(0, y)
        customization_text.write(f"{i + 1}. {color.capitalize()}", align="center", font=("Arial", 20, "normal"))
        y -= 50

    customization_text.goto(0, y - 50)
    customization_text.write("Press a number to select", align="center", font=("Arial", 15, "normal"))

    # Bind color selection keys
    for i, color in enumerate(paddle_colors if item == "paddle" else ball_colors if item == "ball" else background_colors):
        window.onkeypress(lambda c=color: set_color(item, c), str(i + 1))

# Function to show speed menu
def show_speed_menu():
    global customization_text

    customization_text = turtle.Turtle()
    customization_text.speed(0)
    customization_text.color("white")
    customization_text.penup()
    customization_text.hideturtle()
    customization_text.goto(0, 100)
    customization_text.write("Select Game Speed", align="center", font=("Arial", 30, "normal"))

    y = 0
    for i, speed in enumerate(game_speeds):
        customization_text.goto(0, y)
        customization_text.write(f"{i + 1}. {speed.capitalize()}", align="center", font=("Arial", 20, "normal"))
        y -= 50

    customization_text.goto(0, y - 50)
    customization_text.write("Press a number to select", align="center", font=("Arial", 15, "normal"))

    # Bind speed selection keys
    for i, speed in enumerate(game_speeds):
        window.onkeypress(lambda s=speed: set_game_speed(s), str(i + 1))

# Function to set color based on item
def set_color(item, color):
    if item == "paddle":
        set_paddle_color(color)
    elif item == "ball":
        set_ball_color(color)
    elif item == "background":
        set_background_color(color)

    clear_customization_menu()
    show_start_menu()

# Function to display a countdown before starting the game
def countdown():
    global countdown_text

    countdown_text = turtle.Turtle()
    countdown_text.speed(0)
    countdown_text.color("white")
    countdown_text.penup()
    countdown_text.hideturtle()
    countdown_text.goto(0, 0)

    for i in range(3, 0, -1):
        countdown_text.clear()
        countdown_text.write(f"{i}", align="center", font=("Arial", 100, "normal"))
        window.update()
        time.sleep(1)

    countdown_text.clear()
    countdown_text.write("GO!", align="center", font=("Arial", 100, "normal"))
    window.update()
    time.sleep(0.5)
    countdown_text.clear()
    window.update()

# Function to initialize the game
def start_game():
    global start_time, ball

    # Display countdown before starting the game
    countdown()

    start_time = time.time()
    ball.dx = initial_speed
    ball.dy = initial_speed

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
    if game_mode == "single":
        if ball.ycor() > player2.ycor() + 10:
            player2_up()
        elif ball.ycor() < player2.ycor() - 10:
            player2_down()

# Function to toggle pause state
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        score.goto(0, 0)
        score.write("PAUSED", align="center", font=("Arial", 50, "normal"))
    else:
        score.clear()
        score.goto(0, 250)
        score.write(f"Player1: {score1}                Player2: {score2}", align="center", font=(None, 20, "normal"))

# Keyboard bindings
window.listen()
window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")
window.onkeypress(reset_game, "space")
window.onkeypress(start_single_player, "1")
window.onkeypress(start_multiplayer, "2")
window.onkeypress(lambda: show_customization_menu(), "3")  # Bind "3" to show customization menu
window.onkeypress(toggle_pause, "p")  # Bind "P" key to toggle pause

# Bind difficulty selection keys only after the difficulty menu is shown
def bind_difficulty_keys():
    window.onkeypress(lambda: set_difficulty("easy"), "1")
    window.onkeypress(lambda: set_difficulty("medium"), "2")
    window.onkeypress(lambda: set_difficulty("hard"), "3")

# Function to bind customization keys
def bind_customization_keys():
    # Clear existing key bindings
    window.onkeypress(None, "1")
    window.onkeypress(None, "2")
    window.onkeypress(None, "3")
    window.onkeypress(None, "4")

    # Bind keys for paddle color selection
    window.onkeypress(lambda: handle_customization(1), "1")
    window.onkeypress(lambda: handle_customization(2), "2")
    window.onkeypress(lambda: handle_customization(3), "3")
    window.onkeypress(lambda: handle_customization(4), "4")

# Function to reset main menu key bindings
def reset_main_menu_keys():
    # Clear existing key bindings
    window.onkeypress(None, "1")
    window.onkeypress(None, "2")
    window.onkeypress(None, "3")

    # Bind keys for main menu
    window.onkeypress(start_single_player, "1")
    window.onkeypress(start_multiplayer, "2")
    window.onkeypress(lambda: show_customization_menu(), "3")

# Main game loop
def main_game_loop():
    global score1, score2, game_over_flag, start_time
    while True:
        window.update()

        if not paused:  # Skip game logic if paused
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
