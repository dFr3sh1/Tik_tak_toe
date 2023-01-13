

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
print("Tik Tak Toe")
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

