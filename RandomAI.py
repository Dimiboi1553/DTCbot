import random

Board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

winner = 0
posTaken = []
removedpos = -1

def UserInterFace(Board, removedpos, posTaken):
    count = 0
    for i in range(len(Board)):
        if Board[i] == 1:
            count += 1

    if count == 2 and removedpos == -1:
        removedpos = posTaken[0]

    while True:
        UsrChoice = int(input("Where will you put your 1?: "))
        if 1 <= UsrChoice <= 9 and Board[UsrChoice - 1] == 0:
            if removedpos != -1:
                Board[removedpos - 1] = 0  # Remove the '1' at the removedpos
            Board[UsrChoice - 1] = 1
            posTaken.append(UsrChoice)
            return removedpos  # Pass the updated removedpos back
        else:
            print("Error! Invalid move. Try again.")

def ValidateWin(Board, winner):
    # Check rows for a win
    for i in range(0, 9, 3):
        if Board[i] == Board[i + 1] == Board[i + 2] == 1:
            winner = 1
            return True, winner
        elif Board[i] == Board[i + 1] == Board[i + 2] == 2:
            winner = 2
            return True, winner

    # Check columns for a win
    for i in range(3):
        if Board[i] == Board[i + 3] == Board[i + 6] == 1:
            winner = 1
            return True, winner
        elif Board[i] == Board[i + 3] == Board[i + 6] == 2:
            winner = 2
            return True, winner

    # Check diagonals for a win
    if (Board[0] == Board[4] == Board[8] == 1) or (Board[2] == Board[4] == Board[6] == 1):
        winner = 1
        return True, winner
    elif (Board[0] == Board[4] == Board[8] == 2) or (Board[2] == Board[4] == Board[6] == 2):
        winner = 2
        return True, winner

    return False, winner

def printBoard(Board):
    for i in range(0, 9, 3):
        print(Board[i:i+3])

def AI(Board, available_moves, player, depth):
    print("AI")

    # Check for an immediate win
    for move in available_moves:
        copyBoard = list(Board)
        copyBoard[move] = 2
        if ValidateWin(copyBoard, player)[0]:
            Board[move] = 2
            print(move + 1)
            return

    # Check for player's immediate win and block it
    for move in available_moves:
        copyBoard = list(Board)
        copyBoard[move] = 1
        if ValidateWin(copyBoard, 1)[0]:
            Board[move] = 2
            print(move + 1)
            return

    # If no immediate win or block, make a random move
    random_move = random.choice(available_moves)
    Board[random_move] = 2
    print(random_move + 1)

def is_board_full(Board):
    return all(cell != 0 for cell in Board)

# Start the game with the player's turn
while not ValidateWin(Board, winner)[0] and not is_board_full(Board):
    # Player's turn
    if not is_board_full(Board):
        removedpos = UserInterFace(Board, removedpos, posTaken)  # Update removedpos
        printBoard(Board)

        if ValidateWin(Board, winner)[0]:
            if winner == 1:
                print("You win!")
            else:
                print("AI wins!")
            break

        if is_board_full(Board):
            print("It's a draw!")
            break

    # AI's turn
    available_moves = [i for i in range(9) if Board[i] == 0]
    AI(Board, available_moves, 2, depth=3)
    printBoard(Board)

    # Check if the game ended after AI's move
    if ValidateWin(Board, winner)[0]:
        if winner == 1:
            print("You win!")
        else:
            print("AI wins!")
        break

    if is_board_full(Board):
        print("It's a draw!")
        break
#Wins-Draws-Losses
# 0-    0-    0