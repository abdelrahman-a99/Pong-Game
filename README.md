# Pong Game

This is a simple implementation of the classic game Pong using the Turtle module in Python. The game is designed for both single-player and multiplayer modes, and it includes a variety of customization options, difficulty levels, and additional features to enhance the gameplay experience.

## Key Features

- **Game Setup**: The game window, players, ball, and scoring system are set up appropriately. The game window is set to a width of 800 and a height of 600, with a customizable background color. The paddles are colored blue (Player 1) and red (Player 2), and the ball is white. The paddles and ball colors can also be customized.

- **Player Controls**: Keyboard controls allow both players to move their paddles up and down. Player 1 uses the `W` and `S` keys, while Player 2 uses the `Up Arrow` and `Down Arrow` keys. Boundary checks ensure the paddles stay within the playable area.

- **Ball Movement**: The ball moves diagonally at an initial speed that can be customized (default is `0.2` units per frame). The ball bounces off the walls and paddles correctly, and its speed increases dynamically over time.

- **Scoring**: A scoring system keeps track of each player's score. The game ends when one player reaches the target score (set to `5` by default), and the winner is displayed.

- **Game Over**: When the game ends, the ball stops moving, and the winner is announced. A message prompts the players to press the `Spacebar` to reset the game and play again.

- **Boundary Checks**: Boundary checks prevent the ball from moving beyond the top and bottom lines, ensuring it stays within the playable area. The paddles are also constrained to stay within the vertical limits of the screen.

- **Visual Enhancements**: The game includes a center line, a center circle, and a center dot to improve the visual appeal. The top, bottom, left, and right boundaries of the playable area are clearly marked.

- **Single-Player Mode with AI**: The game can be played in single-player mode against an AI opponent. The AI controls the red paddle and adjusts its position based on the ball's movement.

- **Difficulty Levels**: Players can select from three difficulty levels (Easy, Medium, Hard) which affect the initial speed of the ball and the rate at which the speed increases.

- **Customization Options**: Players can customize the game by changing the paddle color, ball color, background color, and game speed.

- **Pause Function**: The game can be paused at any time by pressing the `P` key. This allows players to take a break and resume the game later.

- **Countdown Timer**: A countdown timer is displayed before the game starts, adding a professional touch to the gameplay experience.

## Usage

To run the game, make sure you have Python installed on your system. Clone this repository and execute the `game.py` file using Python.

```bash
python game.py
```

## Controls

- **Player 1 (Blue Paddle)**:
  - Move **Up**: Press the `W` key.
  - Move **Down**: Press the `S` key.

- **Player 2 (Red Paddle)**:
  - Move **Up**: Press the `Up Arrow` key.
  - Move **Down**: Press the `Down Arrow` key.

- **Reset Game**:
  - Press the `Spacebar` to reset the game after a game over.

- **Pause Game**:
  - Press the `P` key to pause or resume the game.

- **Start Single-Player Mode**:
  - Press the `1` key to start the game in single-player mode.

- **Start Multiplayer Mode**:
  - Press the `2` key to start the game in multiplayer mode.

- **Customization Menu**:
  - Press the `3` key to access the customization menu, where you can change paddle color, ball color, background color, and game speed.

- **Select Difficulty Level**:
  - Press the `1`, `2`, or `3` keys to select Easy, Medium, or Hard difficulty, respectively.

- **Go Back**:
  - Press the `Escape` key to go back to the main menu from any submenu.

## Customization Options

- **Paddle Color**: Choose from a variety of colors for both paddles.

- **Ball Color**: Customize the ball's color.

- **Background Color**: Change the background color of the game window.

- **Game Speed**: Adjust the game speed to slow, normal, or fast.

## Future Enhancements

Here are some ideas for future enhancements to the game:

- **Sound Effects**: Add sound effects for ball hits, scoring, and game over.
- **Power-ups**: Introduce power-ups that can change the ball's speed, paddle size, or other game dynamics.
- **Visual Enhancements**: Add more visual effects, such as trails behind the ball or animated backgrounds.
- **Customizable Controls**: Allow players to customize the control keys.
- **High Score System**: Implement a high score system to track the best scores.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

Enjoy the game!