from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("+-------+-------+-------+")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("+-------+-------+-------+")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("+-------+-------+-------+")

def check_rows(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True
    return False

def check_columns(board, mark):
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == mark:
            return True
    return False

def check_diagonals(board, mark):
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def is_game_over(board):
    if check_rows(board, 'X') or check_columns(board, 'X') or check_diagonals(board, 'X'):
        display_board(board)
        print("PC wins!")
        return True
    if check_rows(board, 'O') or check_columns(board, 'O') or check_diagonals(board, 'O'):
        display_board(board)
        print("Player wins!")
        return True
    # Check for draw: no cell contains an integer (all are 'X' or 'O')
    free_cells = any(isinstance(board[r][c], int) for r in range(3) for c in range(3))
    if not free_cells:
        display_board(board)
        print("Draw!")
        return True
    return False

def user_move(board):
    while True:
        try:
            a = int(input("Enter your move (1–9): "))
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        if a < 1 or a > 9:
            print("Invalid number. Choose between 1 and 9.")
            continue

        row = (a - 1) // 3   # 0, 1, or 2
        col = (a - 1) % 3    # 0, 1, or 2

        if isinstance(board[row][col], int):
            board[row][col] = 'O'
            return
        else:
            print("Cell occupied. Try another.")

def pc_move(board):
    while True:
        move = randrange(1, 10)  # random integer from 1 to 9
        row = (move - 1) // 3
        col = (move - 1) % 3
        if isinstance(board[row][col], int):
            board[row][col] = 'X'
            return

if __name__ == "__main__":
    # PC starts in the center
    board = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
    ]

    while True:
        display_board(board)

        # Check end of game before player's move
        if is_game_over(board):
            break

        user_move(board)

        # Check end of game after player's move
        if is_game_over(board):
            break

        pc_move(board)

        # Check end of game after PC's move
        if is_game_over(board):
            break
