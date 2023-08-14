def ConstBoard(Board):
    print("Current State of the Board: \n\n")
    for i in range(0, 9):
        if (i != 0) and (i % 3 == 0):
            print("\n")
        if Board[i] == 0:
            print("_", end=" ")
        elif Board[i] == -1:
            print("X", end=" ")
        elif Board[i] == 1:
            print("O", end=" ")

def User1Turn(Board):
    pos = input("Enter X's position from [1,2,3,......9]")
    pos = int(pos)
    if Board[pos - 1] != 0:
        print("Wrong Move")
        exit(0)
    Board[pos - 1] = -1

def User2Turn(Board):
    pos = input("Enter O's position from [1,2,3,......9]")
    pos = int(pos)
    if Board[pos - 1] != 0:
        print("Wrong Move")
        exit(0)
    Board[pos - 1] = 1

def CompTurn(Board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if Board[i] == 0:
            Board[i] = 1
            score = -minmax(Board, -1)
            Board[i] = 0
            if score > value:
                value = score
                pos = i
    Board[pos] = 1

def minmax(Board, player):
    x = analyzeboard(Board)
    if x != 0:
        return x * player
    pos = -1
    value = -2
    for i in range(0, 9):
        if Board[i] == 0:
            Board[i] = player
            score = -minmax(Board, -player)
            Board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value

def analyzeboard(Board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if Board[cb[i][0]] != 0 and Board[cb[i][0]] == Board[cb[i][1]] and Board[cb[i][0]] == Board[cb[i][2]]:
            return Board[cb[i][0]]
    return 0

def main():
    choice = input("Enter 1 for Singleplayer, Enter 2 for Multiplayer")
    choice = int(choice)
    Board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if choice == 1:
        print("Computer: O Vs. Player: X")
        for i in range(0, 9):
            if analyzeboard(Board) != 0:
                break
            if i % 2 == 0:
                ConstBoard(Board)
                User1Turn(Board)
            else:
                ConstBoard(Board)
                CompTurn(Board)
    else:
        for i in range(0, 9):
            if analyzeboard(Board) != 0:
                break
            if i % 2 == 0:
                ConstBoard(Board)
                User2Turn(Board)
            else:
                ConstBoard(Board)
                User1Turn(Board)
    x = analyzeboard(Board)
    if x == 0:
        ConstBoard(Board)
        print("\nDraw !!!")
    elif x == -1:
        ConstBoard(Board)
        print("\nPlayer X WON !!! Player O lost!")
    elif x == 1:
        ConstBoard(Board)
        print("\nPlayer O WON !!! Player X lost!")
main()
