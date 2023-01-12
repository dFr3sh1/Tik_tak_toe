
dico = {
        "A" : ["_", "_", "_"],
        "B" : ["_", "_", "_"],
        "C" : ["_", "_", "_"]
    }

def show_grid(grid):
    """This funcion will show the grid and needs three paramaters : 
    * grid
    * player
    * play

    Args:
        grid (_type_): _description_
    """
    
    for line in grid:
        for elt in grid[line]:
            print(" ", elt, " |", end = "")
        print("\n")
        
def valid_play(grid, val_user) -> bool:
    if val_user[0].upper() in ["A", "B", "C"] and int(val_user[1]) in [1, 2, 3]:
        if grid[val_user[0].upper()][int(val_user[1])] == "_":
            return True
    return False

def play(grid, val_user, player):
    move = input("Entrez votre coup : ")

player = "X"
End_game = False

while not End_game:
    show_grid(dico)
    print("Le joueur en cours est ", player)
    play(dico, "B2","X")
    while not valid_play(dico, play):
        play()


        
# def can_be_played() -> bool:
#     counter = 0
#     val_user = input("Entrez votre coup : ")
    
    
#     while valid_play() != True and counter < 2:
#         val_user = input("Entrez votre coup en suivant les instructions : ")
#         counter += 1
#         if counter > 1:
#             print("Désolé, vous n'avez pas compris le jeu.")
        
#     pass

show_grid(dico)

can_be_played(dico)

# board = ["-"] * 9

# # Function to display the board
# def display_board():
#     for i in range(0, 9, 3):
#         print(board[i] + " | " + board[i+1] + " | " + board[i+2])
#         if i < 6:
#             print("---------")

# # Function to handle player moves
# def player_move(player):
#     while True:
#         try:
#             move = int(input("Player " + player + ", enter your move (1-9): "))
#             if move >= 1 and move <= 9:
#                 if board[move-1] == "-":
#                     board[move-1] = player
#                     break
#                 else:
#                     print("That space is already occupied, please choose another.")
#             else:
#                 print("Invalid move, please enter a number between 1 and 9.")
#         except ValueError:
#             print("Invalid input, please enter a number between 1 and 9.")

# # Function to check for a winner
# def check_winner():
#     if board[0] == board[1] == board[2] != "-":
#         return board[0]
#     elif board[3] == board[4] == board[5] != "-":
#         return board[3]
#     elif board[6] == board[7] == board[8] != "-":
#         return board[6]
#     elif board[0] == board[3] == board[6] != "-":
#         return board[0]
#     elif board[1] == board[4] == board[7] != "-":
#         return board[1]
#     elif board[2] == board[5] == board[8] != "-":
#         return board[2]
#     elif board[0] == board[4] == board[8] != "-":
#         return board[0]
#     elif board[2] == board[4] == board[6] != "-":
#         return board[2]
#     elif "-" not in board:
#         return "Tie"
#     else:
#         return None

# # Main game loop
# print("Welcome to Tic-tac-toe!")
# while True:
#     display_board()
#     player_move("X")
#     display_board()
#     winner = check_winner()
#     if winner:
#         print(winner + " wins!")
#         break
#     player_move("O")
#     winner = check_winner()
#     if winner:
#         display_board()
#         print(winner + " wins!")
#         break