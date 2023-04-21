# ia.py
def ia(board, signe):
    # Vérifie si l'IA peut gagner au prochain coup
    for i in range(9):
        if board[i] == 0:
            board[i] = signe
            if check_winner(board):
                return i
            board[i] = 0

    # Vérifie si l'adversaire peut gagner au prochain coup et bloque son coup
    for i in range(9):
        if board[i] == 0:
            board[i] = 3 - signe
            if check_winner(board):
                board[i] = signe
                return i
            board[i] = 0

    # Joue au centre si la case est libre
    if board[4] == 0:
        return 4

    # Joue dans un coin si une case est libre
    for i in [0, 2, 6, 8]:
        if board[i] == 0:
            return i

    # Joue dans une case libre quelconque
    for i in range(9):
        if board[i] == 0:
            return i

    # Aucun coup possible
    return False

def check_winner(board):
    # Vérifie les lignes
    for i in range(3):
        if board[3*i] == board[3*i+1] == board[3*i+2] and board[3*i] != 0:
            return True

    # Vérifie les colonnes
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != 0:
            return True

    # Vérifie les diagonales
    if board[0] == board[4] == board[8] and board[0] != 0:
        return True
    if board[2] == board[4] == board[6] and board[2] != 0:
        return True

    return False