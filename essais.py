scores = {}
    for i in board.keys():
        if board[i] == "  ":
            board[i] = "o"
            scores[i] = minimax(board, 100 , False)
            board[i] = "  "
    best_move = max(scores, key=scores.get)
    button = buttons[best_move-1]
    button["text"] = "O"
    board[best_move] = "o"
    if win(turn) :
        winLabel = Label(frame1 , text="L'IA a gagné la partie",font=("Arial",25), bg="gray",width=18)
        winLabel.grid(row= 0 , column= 0 , columnspan= 3)
        fin_jeu = True
    elif checkgamenulle():
        nulleLabel = Label(frame1 , text= "Partie nulle" ,font=("Arial",25), bg="gray",width=18)
        nulleLabel.grid(row= 0 , column= 0 , columnspan= 3)
        fin_jeu = True
    turn = "x"
    if turn ==  "x":
        button = event.widget
        buttontext = str(button)
        clicked = buttontext[-1]
        print(clicked)
        if clicked == "n":
            clicked = 1
        else:
            clicked = int(clicked)
    
        button["text"]= "X"
        board[clicked] = turn
        if win(turn) :
                winLabel = Label(frame1 , text=f"{turn} a gagne la partie",font=("Arial",25),bg="gray",width=18)
                winLabel.grid(row= 0 , column= 0 , columnspan= 3)
                fin_jeu = True

def minimax(board, depth, isMaximizing):
    if win("o"):
        return 1
    elif win("x"):
        return -1
    elif checkgamenulle():
        return 0
    
    if isMaximizing:
        bestScore = -1
        for i in board.keys():
            if board[i] == "  ":
                board[i] = "o"
                score = minimax(board, depth+1, False)
                board[i] = "  "
                bestScore = max(score, bestScore)
        return bestScore
    
    else:
        bestScore = 10
        for i in board.keys():
            if board[i] == "  ":
                board[i] = "x"
                score = minimax(board, depth+1, True)
                board[i] = "  "
                bestScore = min(score, bestScore)
        return bestScore
def ia(board, signe):
    # Vérifier que le signe est valide
    if signe != "X" and signe != "O":
        return False
    
    # Choisir une case aléatoire
    import random
    while True:
        case = random.randint(0, 8)
        if board[case] == 0:
            return case
print(ia(board, signe))



def minimax(board, depth, isMaximizing):
    if win("o"):
        return 1
    elif win("x"):
        return -1
    elif checkgamenulle():
        return 0
    
    if isMaximizing:
        bestScore = -10
        for i in board.keys():
            if board[i] == "v":
                board[i] = "o"
                score = minimax(board, depth+1, False)
                board[i] = "v"
                bestScore = max(score, bestScore)
        return bestScore
    
    else:
        bestScore = 10
        for i in board.keys():
            if board[i] == "v":
                board[i] = "x"
                score = minimax(board, depth+1, True)
                board[i] = "v"
                bestScore = min(score, bestScore)
        return bestScore