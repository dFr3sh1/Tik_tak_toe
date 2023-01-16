plateau = {
    "A" : [None for _ in range(3)],
    "B" : [None for _ in range(3)],
    "C" : [None for _ in range(3)]    
}

def afficher_grille(plateau:dict) -> None:
    """Fonction qui affiche la grille du jeu Morpion

    Args:
        plateau (dict): un plateau de jeu
    """
    
for cle in plateau:
    print(cle, end="\t|\t")
    for elt in plateau[cle]:
        if elt == None:
            print(" ", end='\t|\t')
        else:
            print(elt, end="\t|\t")
    print("\n---------------------------------------------------------")
    
    
def jouer_coup(plateau:dict, joueur:str, coup:str) -> None:
    """Fonction qui joue un coup (Ne vérifie pas si le coup est valide)

    Args:
        platea (dict): Le plateau du jeu
        joueur (str): "O" ou "X"
        coup (str): Coordonnées de la forme "A1"
    """
    plateau[coup[0]][int(coup[1])] = joueur == None:
    return True


    