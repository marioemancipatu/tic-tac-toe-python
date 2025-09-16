# Tic-Tac-Toe Python

This is a simple console-based Tic-Tac-Toe game written in Python. In this game, the player plays with 'O' and the computer plays with 'X'. The computer always starts with its first move in the center of the board.

# How the Game Works

- The board is displayed as a 3x3 grid, with numbers 1 to 9 representing the positions:
```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```
- The computer always makes the first move, placing an 'X' in the middle of the board.
- The player chooses their move by entering the number corresponding to an empty square.
- The computer makes its moves randomly on available positions.
- The game checks after every move if the player or computer has won.
- The game ends when either the player or computer wins, or if all squares are filled, resulting in a tie.

# Features

- Simple text-based board display with clear formatting.
- Player vs Computer gameplay with alternating turns.
- Input validation to prevent invalid moves or choosing occupied squares.
- Automatic detection of wins, losses, and ties.
- No artificial intelligence; the computer chooses moves randomly for simplicity.

# Example of a Board

At the start of the game:
```
+-------+-------+-------+
|       |       |       |
|  1    |  2    |  3    |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  4    |  X    |  6    |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  7    |  8    |  9    |
|       |       |       |
+-------+-------+-------+
```

During gameplay:
```
+-------+-------+-------+
|       |       |       |
|  1    |  O    |  3    |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  4    |  X    |  6    |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  7    |  8    |  X    |
|       |       |       |
+-------+-------+-------+
```

# Requirements

- Python 3.x

# Author

Mario Emancipatu

