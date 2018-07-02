import random

def drawBoard(board):

    print('|     |' + '      |' + '      |')
    print('|  ' + board[7] + '  |' + '   ' + board[8] + '  |' + '   ' + board[9] + '  |' )
    print('|-----|' + '------|' + '------|')
    print('|     |' + '      |' + '      |')
    print('|  ' + board[4] + '  |' + '   ' + board[5] + '  |' + '   ' + board[6] + '  |' )
    print('|-----|' + '------|' + '------|')
    print('|     |' + '      |' + '      |')
    print('|  ' + board[1] + '  |' + '   ' + board[2] + '  |' + '   ' + board[3] + '  |' )



#asking player to choose his role

def inputPlayerLetter():
    marker = ''
    while not ( marker == 'X' or marker == 'O'):
        print('Do you want to be X or O?')
        marker = input().upper()

    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O','X']


#Deciding who goes first
#Randomly choose the player who goes first
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

#Asking the player whether to continue with the game or not

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


#placing the mark on the board
def makeMove(board,marker,position):
    board[position] = marker

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == bo[9] == le) or
            (bo[4] == le and bo[5] == bo[6] == le) or
            (bo[1] == le and bo[2] == bo[3] == le) or
            (bo[7] == le and bo[4] == bo[1] == le) or
            (bo[8] == le and bo[5] == bo[2] == le) or
            (bo[9] == le and bo[6] == bo[3] == le) or
            (bo[7] == le and bo[5] == bo[3] == le) or
            (bo[9] == le and bo[5] == bo[1] == le))

#duplicating the board data

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

#checking if a space on the board is free

def isSpaceFree(board, move):
    return board[move] == ' '

#Letting the player enter their position

def getPlayerMove(board):
    move = 0
    while move not in [1,2,3,4,5,6,7,8,9] or not isSpaceFree(board, move):
        move = int(input('What is your next move? (1-9)'))
    return move

#choosing a move from the list of moves
def chooseRandomMoveFromList(board, positionList):
    possibleMoves = []
    for i in positionList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return  random.choice(possibleMoves)
        else:
            return None
#Creating the computers AI
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #algorithm for AI
    #checking first, if AI can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    #checking if the player could win on their next move, block the move

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #checking the corner, center, side space
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    #Try to take the center, if it is free
    if isSpaceFree(board, 5):
        return 5
    #Move on one of the sides
    return chooseRandomMoveFromList(board, [2,4,6,8])


#CHECKING IF THE BOARD IS FULL
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True


#Starting the game
print('Welcome Tic Tac Toe python version!')

while True:
    theBoard = [' ']*10
    # Deciding the palyer's mark and who goes first
    playerLetter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    #Running the player's turn
    while gameIsPlaying:
        if turn == 'player':
            #playerturn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            #checking if the player is won
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            #checking if the board is full after player's move
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        elif turn == 'computer':
            #computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You Lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'


    if not playAgain():
            break

