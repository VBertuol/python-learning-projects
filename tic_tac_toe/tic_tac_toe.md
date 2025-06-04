# PROJECT: Tic-Tac-Toe

## Scenario

Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

- The computer (i.e., your program) should play the game using **'X'**s.
- The user (e.g., you) should play the game using **'O'**s.
- The first move belongs to the computer – it always puts its first **'X'** in the middle of the board.
- All the squares are numbered row by row starting with **1** (see the example session below for reference).
- The user inputs their move by entering the number of the square they choose – the number must be valid, i.e., it must:
  - Be an integer.
  - Be greater than **0** and less than **10**.
  - Not point to a field which is already occupied.
- The program checks if the game is over – there are four possible verdicts:
  1. The game should continue.
  2. The game ends with a tie.
  3. You (the user) win.
  4. The computer wins.
- The computer responds with its move and the check is repeated.
- Don’t implement any form of artificial intelligence – a random field choice made by the computer is good enough for the game.

---

## Example Session

```text
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1

+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 8

+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+

+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 4

+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+

+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 7

+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
You won!
```

---

## Requirements

1. **Board Representation**  
   - The board should be stored as a three-element list, where each element is another three-element list (the inner lists represent rows).  
   - All of the squares may be accessed using the following syntax:  
     ```python
     board[row][column]
     ```  
   - Each of the inner list’s elements can contain:
     - **'O'**, **'X'**, or
     - A digit representing the square’s number (such a square is considered free).

2. **Board Appearance**  
   - The board’s appearance should be exactly the same as the one presented in the example session above.

3. **Function Implementation**  
   - Implement the functions defined for you in the editor.

---

## Note on Random Moves

Drawing a random integer number can be done by utilizing a Python function called `randrange()`. The example program below shows how to use it (the program prints ten random numbers from 0 to 8):

```python
from random import randrange

for i in range(10):
    print(randrange(8))
```

> **Note:** The `from ... import` instruction provides access to the `randrange` function defined within an external Python module called `random`.