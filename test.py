board = ["-"] * 9

def display_board():
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---------")

display_board()