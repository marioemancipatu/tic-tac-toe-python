import random

board = [[str(3*r +c +1) for c in range(3)] for r in range(3)]

board[1][1] = 'X'

def display_board(board):
   
    print("+-------+-------+-------+")
    for r in range(3):
        print("|       |       |       |")
        print(f"|  {board[r][0]}  |  {board[r][1]}  |  {board[r][2]}  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

display_board(board)

def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        
        if move not in [str(n) for n in range(1, 10)]:
            print("Invalid move. Enter a number between 1 and 9.")
            continue

        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        
        if board[row][col] in ('X', 'O'):
            print("Cell already occupied. Choose another move.")
            continue

        
        board[row][col] = 'O'
        break


def make_list_of_free_fields(board):
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ('X', 'O'):
                free_fields.append((r,c))
    return free_fields


def draw_move(board):
    free = make_list_of_free_fields(board)
    move = random.choice(free)
    row, col = move
    board[row][col] = 'X'


def victory_for(board, sign):
    for r in range(3):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True
    for c in range(3):
        if board[0][c] == sign and board[1][c] == sign and board[2][c] == sign:
            return True 
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False


while not victory_for(board, 'X') and not victory_for(board, 'O') and len(make_list_of_free_fields(board)) > 0:
    display_board(board)        
    enter_move(board)           
    if victory_for(board, 'O'): 
        display_board(board)
        print("You win!")
        break
    if len(make_list_of_free_fields(board)) == 0:  
        display_board(board)
        print("It's a tie!")
        break
    draw_move(board)            
    if victory_for(board, 'X'): 
        display_board(board)
        print("Computer wins!")
        break
