import sys

# Original board for playing.
orgBoard = []

# Assigning play Letter's to players.
playerOne = 'X'  # Human
playerTwo = 'O'  # Bot

# Initializing board with "#".


def createBoard():
    for i in range(0, 9):
        orgBoard.append("#")

# Prints the board in formated output.


def printBoard(bd=orgBoard):
    for i in range(0, 9):
        if i % 3 == 0:
            print()
        print("  {}  ".format(bd[i]), end="")

    print()

# Checks for the win condition provided current state of board and player (One/Two).
# Returns true if win.


def win(player, board):
    win = False
    if board[0] == board[1] and board[0] == board[2] and board[0] == player:
        win = True
    elif board[3] == board[4] and board[3] == board[5] and board[3] == player:
        win = True
    elif board[6] == board[7] and board[6] == board[8] and board[6] == player:
        win = True
    elif board[0] == board[3] and board[0] == board[6] and board[0] == player:
        win = True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == player:
        win = True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == player:
        win = True
    elif board[0] == board[4] and board[0] == board[8] and board[0] == player:
        win = True
    elif board[2] == board[4] and board[2] == board[6] and board[2] == player:
        win = True

    return win

# Interface for human player to play.


def choosePos():
    while True:
        pos = int(input("Enter the position you want to play:- ").strip()) - 1
        if orgBoard[pos] == "#":
            orgBoard[pos] = playerOne
            return pos
        else:
            print('Position already Filled')

# Tested Till this point everythings works perfectly fine.

# This provides the AI to the game.
# This takes one argument which is the prediction play list.
# This list provides a sequence such that major play flow decisions can be taken on the
# basis of this list. For moves like first move , there is no need to check whether someone is
# Winning or not as that is not possible without atleast two positions existing.


def bot(gameList):
    # twoWin is a flag which is used to indicate whether some move exists in which playerTwo wins the
    # game.
    twoWin = False

    # flag is used to indicate whether any of playerOne or playerTwo wins. If so then True.
    flag = False

    if len(gameList) > 6:
        orgBoard[gameList[0]] = playerTwo
        returnVal = gameList[0]
    else:
        # Creating a copy of the original board.
        board = orgBoard[:]
        # This performs a brute force sequencial with all available positions
        # for conditions that indicate playerTwo wins and chooses the first one it finds.
        for i in gameList:
            board[i] = playerTwo
            check = win(playerTwo, board)
            if check:
                flag = True
                twoWin = True
                orgBoard[i] = playerTwo
                returnVal = i
                break
            else:
                board[i] = "#"

        # This condition only works when playerTwo doesn't win.
        if not twoWin:
            for i in gameList:
                board[i] = playerOne
                check = win(playerOne, board)
                if check:
                    flag = True
                    orgBoard[i] = playerTwo
                    returnVal = i
                    break
                else:
                    board[i] = "#"

    # Condition occurs when neither of player's win.
    # Choose first position from gameList.
    if flag == False:
        returnVal = gameList[0]
        orgBoard[returnVal] = playerTwo

    # Returns the position of element played and whether playerTwo wins or not as a tuple.
    return (returnVal, twoWin)


def main():
    createBoard()
    printBoard()
    gameList = [4, 1, 8, 2, 0, 6, 3, 5, 7]
    # Decide which player get's the first turn and to do that , use random.
    # For testing purpose , one always goes first.
    while len(gameList) > 0:
        print("", end="\n")
        pos = choosePos()
        printBoard()
        gameList.remove(pos)
        check = win(playerOne, orgBoard)
        if check:
            print()
            print(playerOne, 'Won the game')
            sys.exit(0)
        else:
            print()
            if len(gameList) > 0:
                val, verify = bot(gameList)
                gameList.remove(val)
                if verify:
                    printBoard()
                    print("You Lose")
                    sys.exit(0)
                printBoard()

    print('It is a draw. Thank you for playing')


if __name__ == '__main__':
    main()
