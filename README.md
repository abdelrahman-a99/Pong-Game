# Pong Game

This is a simple implementation of the classic game Pong using the Turtle module in Python. The game is designed for two players and includes all the basic mechanics of the original Pong game, along with some additional features.

## Key Features

- **Game Setup**: The game window, players, ball, and scoring system are set up appropriately. The game window is set to a width of 800 and a height of 600, with a black background. The paddles are colored blue (Player 1) and red (Player 2), and the ball is white.

- **Player Controls**: Keyboard controls allow both players to move their paddles up and down. Player 1 uses the `W` and `S` keys, while Player 2 uses the `Up Arrow` and `Down Arrow` keys. Boundary checks ensure the paddles stay within the playable area.

- **Ball Movement**: The ball moves diagonally at an initial speed of `0.2` units per frame and bounces off the walls and paddles correctly. The ball's speed increases dynamically after each paddle hit.

- **Scoring**: A scoring system keeps track of each player's score. The game ends when one player reaches the target score (set to `5` by default), and the winner is displayed.

- **Game Over**: When the game ends, the ball stops moving, and the winner is announced. A message prompts the players to press the `Spacebar` to reset the game and play again.

- **Boundary Checks**: Boundary checks prevent the ball from moving beyond the top and bottom lines, ensuring it stays within the playable area. The paddles are also constrained to stay within the vertical limits of the screen.

- **Visual Enhancements**: The game includes a center line, a center circle, and a center dot to improve the visual appeal. The top, bottom, left, and right boundaries of the playable area are clearly marked.

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

## Future Enhancements

Here are some ideas for future enhancements to the game:

- **Sound Effects**: Add sound effects for ball hits, scoring, and game over.
- **AI Opponents**: Implement an AI opponent for single-player mode.
- **Difficulty Levels**: Add different difficulty levels to adjust the speed and behavior of the ball.
- **Power-ups**: Introduce power-ups that can change the ball's speed, paddle size, or other game dynamics.
- **Visual Enhancements**: Add more visual effects, such as trails behind the ball or animated backgrounds.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

Enjoy the game!