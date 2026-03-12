board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]


def print_board():
    for row in board:
        print(" ".join(row))
    print()


def evaluate():
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "_":
            if board[row][0] == "x":
                return 10
            else:
                return -10

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "_":
            if board[0][col] == "x":
                return 10
            else:
                return -10

    
    if board[0][0] == board[1][1] == board[2][2] != "_":
        if board[0][0] == "x":
            return 10
        else:
            return -10

    if board[0][2] == board[1][1] == board[2][0] != "_":
        if board[0][2] == "x":
            return 10
        else:
            return -10

    return 0


def moves_left():
    for row in board:
        if "_" in row:
            return True
    return False


player = "x"

while True:
    print_board()

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] != "_":
        print("Cell already taken\n")
        continue

    board[row][col] = player

    score = evaluate()

    if score == 10:
        print_board()
        print("Player X Wins")
        break

    if score == -10:
        print_board()
        print("Player O Wins")
        break

    if not moves_left():
        print_board()
        print("Game Draw")
        break

    
    if player == "x":
        player = "o"
    else:
        player = "x"