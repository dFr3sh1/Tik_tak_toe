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

#Verification des lignes
for cle in plateau:
    if plateau[cle][0] == plateau[cle][1] == plateau[cle][2] and plateau[cle][0] != None:
        return True


def is_filled(plateau:dict) -> bool:
    """ Fonction qui permet de voir si la grille est pleine

    Args:
        plateau (dict): un plateau de jeu

    Returns:
        bool: True si la grille est pleine. False  sinon
    """
    
    for cle in plateau:
        for case in plateau[cle]:
            if case == None:
                return False
    return True

ended = False
joueur = "X"

while not ended:
    afficher_grille(plateau)
    jouer_coup = input("Rentrez un coup")
    while not
        jouer_coup = input("Rentrez un coup")