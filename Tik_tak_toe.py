grid = ["-"] * 9

def display_grid():
    """This funcion will show the grid and needs grid paramater : 
    * grid

    Args:
        board (_type_): _description_
    """
    for i in range(0, 9, 3):
        print(grid[i] + " | " + grid[i+1] + " | " + grid[i+2])
        if i < 6:
            print("---------")
            
def valid_move(player):
    """Cette fonction evalue si le coup est valide.
    Elle prends en compte deux paramètres, grid et joueur

    Args:
        player (_type_): _description_
    """
    while True:
        try:
            move = int(input("Joueur" + player + " , entrez votre coup (1-9) : "))
            if move >= 1 and move <= 9:
                if grid[move - 1] == "-":
                    grid[move - 1] = player
                    break
                else:
                    print("Cette case est déjà occupée, choisissez une autre case.")
            else:
                print("Entrez votre coup en suivant les instructions (1-9).")
        except ValueError:
            print("Entrez votre coup en suivant les instructions (1-9).")
            
def check_winner():
    """Cette function evalue si 3 des icon de joueurs sont alignés sans interruption.
    Elle a besoin de grid comme argument 

    Returns:
        _type_: _description_
    """
    if grid[0] == grid[1] == grid[2] != "-":
        return grid[0]
    elif grid[3] == grid[4] == grid[5] != "-":
        return grid[3]
    elif grid[6] == grid [7]  == grid[8] != "-":
        return grid[6]
    elif grid[0] == grid[3] == grid[6] != "-":
        return grid[0]
    elif grid[1] == grid[4] == grid[7] != "-":
        return grid[1]
    elif grid[2] == grid[5] == grid[8] != "-":
        return grid[2]
    elif grid[0] == grid[4] == grid[8] != "-":
        return grid[0]
    elif grid[2] == grid[4] == grid[6] != "-":
        return grid[2]
    elif "-" not in grid:
        return "Match null"
    else:
        return None
  
print("Tik Tak Toe, Joe !")
while True:
    display_grid()
    valid_move(" X")
    display_grid()
    winner = check_winner()
    if winner:
        print(winner + " Gagnant.e !")
        break
    valid_move(" O")
    winner = check_winner()
    if winner:
        display_grid()
        print(winner + " Gagnant.e !")
        break