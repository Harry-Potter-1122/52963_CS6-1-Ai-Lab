import tkinter as tk
from tkinter import messagebox

board = [["_" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

player = "x"


def evaluate():
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "_":
            return 10 if board[row][0] == "x" else -10

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return 10 if board[0][col] == "x" else -10

    
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return 10 if board[0][0] == "x" else -10

    
    if board[0][2] == board[1][1] == board[2][0] != "_":
        return 10 if board[0][2] == "x" else -10

    return 0


def is_moves_left():
    for row in board:
        if "_" in row:
            return True
    return False


def click(row, col):
    global player

    if board[row][col] == "_":
        board[row][col] = player
        buttons[row][col]["text"] = player

        score = evaluate()

        if score == 10:
            messagebox.showinfo("Game Over", "Player X Wins")
            reset_board()
            return

        if score == -10:
            messagebox.showinfo("Game Over", "Player O Wins")
            reset_board()
            return

        if not is_moves_left():
            messagebox.showinfo("Game Over", "Draw")
            reset_board()
            return

        
        player = "o" if player == "x" else "x"


def reset_board():
    global board, player

    board = [["_" for _ in range(3)] for _ in range(3)]
    player = "x"

    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""


root = tk.Tk()
root.title("Tic Tac Toe - AI Lab")

for i in range(3):
    for j in range(3):
        btn = tk.Button(root,
                        text="",
                        font=("Arial", 20),
                        width=6,
                        height=3,
                        command=lambda r=i, c=j: click(r, c))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

root.mainloop()