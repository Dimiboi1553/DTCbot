import random

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

def AI_Player1(Board, available_moves, player, depth):
    # Check for an immediate win
    for move in available_moves:
        copyBoard = list(Board)
        copyBoard[move] = 1
        if ValidateWin(copyBoard, player)[0]:
            Board[move] = 1
            return

    # Check for opponent's immediate win and block it
    for move in available_moves:
        copyBoard = list(Board)
        copyBoard[move] = 2
        if ValidateWin(copyBoard, 2)[0]:
            Board[move] = 1
            return

    # If no immediate win or block, make a random move
    random_move = random.choice(available_moves)
    Board[random_move] = 1

def AI_Player2(Board, available_moves, player, depth):
    # Check for an immediate win
    for move in available_moves:
        copyBoard = list(Board)
        copyBoard[move] = 2
        if ValidateWin(copyBoard, player)[0]:
            Board[move] = 2
            return

    # Check for player's immediate win and block it
    for move in available_moves:
        copyBoard = list(Board)
        copyBoard[move] = 1
        if ValidateWin(copyBoard, 1)[0]:
            Board[move] = 2
            return

    copyBoard = list(Board)

    for move in available_moves:
        FirstPCMove = move

        for _ in range(depth):
            copyBoard = list(Board)
            copyBoard[FirstPCMove] = 2

            if ValidateWin(copyBoard, player)[0]:
                Board[FirstPCMove] = 2
                return

            for player_move in available_moves:
                copyBoard[player_move] = 1
                if ValidateWin(copyBoard, 1)[0]:
                    return

                copyBoard[player_move] = 0

            if player == 2:
                ai_available_moves = [i for i in range(9) if copyBoard[i] == 0]
                copyBoard[random.choice(ai_available_moves)] = 2

                if ValidateWin(copyBoard, player)[0]:
                    Board[FirstPCMove] = 2
                    return

            available_moves = [i for i in range(9) if Board[i] == 0]
            if player == 1:
                copyBoard[random.choice(available_moves)] = 1

def is_board_full(Board):
    return all(cell != 0 for cell in Board)

V2Wins = 0
V1Wins = 0
Draws = 0

# Simulate AI Player 1 vs AI Player 2 for 100 games
for i in range(1000):
    Board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    winner = 0

    while not ValidateWin(Board, winner)[0] and not is_board_full(Board):
        # AI Player 1's turn
        if not is_board_full(Board):
            AI_Player2(Board, [i for i in range(9) if Board[i] == 0], 1, depth=3)

            if ValidateWin(Board, winner)[0]:
                if winner == 1:
                    V1Wins += 1
                else:
                    V2Wins += 1
                break

            if is_board_full(Board):
                Draws += 1
                break

        # AI Player 2's turn
        if not is_board_full(Board):
            AI_Player1(Board, [i for i in range(9) if Board[i] == 0], 2, depth=3)

            if ValidateWin(Board, winner)[0]:
                if winner == 1:
                    V1Wins += 1
                else:
                    V2Wins += 1
                break

            if is_board_full(Board):
                Draws += 1
                break

print("AI Player 1 Wins: ", V1Wins)
print("AI Player 2 Wins: ", V2Wins)
print("Draws: ", Draws)
