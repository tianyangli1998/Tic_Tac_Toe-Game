import random
def drawBoard(board):
    """
    This function prints out the board that it was passed.
    Board is a list of 10 strings representing the board (ignore index 0)
    The board is numbered like the keyboard's number pad.
    """
    blankline = (' '*3 + '|')*2 + ' '*3 
    horizon = '-' * 11
    for i in range(1, 10):
        if i%3 == 1:
            print(blankline)
        print(' ' + board[i] + ' ', end='')
        if i%3 !=0:
            print('|', end='')
        else:
            print()
            print(blankline)
            if i != 9:
                print(horizon)
# the following codes are used to test the drawBoard function
theBoard = ['X'] *10
drawBoard(theBoard)
# the output of the drawBoard function is the following

def inputPlayerLetter():
    """
    Lets the player type which letter ('X' or 'O') they want to be.
    Returns a list with the player's letter as the first item, 
    and the computer's letter as the second.
    
    """
    # set the user's input to letter
    # if letter is neither 'X' nor 'O', ask user to input again
    # until letter is 'X' or 'O'
    while True:
        c = input('Do you want to be X or O?\n')
        c = c.lower()
        if c in ['o', 'x']:
            break
        print("Please input 'X' or 'O'!")
    # if letter is 'X', return ['X','O']
    # else return ['O','X']
    return ['X', 'O'] if c == 'x' else ['O', 'X']

# the following codes are used to test the inputPlayerLetter function
# playerLetter, computerLetter = inputPlayerLetter()
# print('Player chooses ', playerLetter)
# print('Computer chooses ', computerLetter)

def whoGoesFirst():
    """ 
    randomly choose the player who goes first
    """
    # use the randint function in random module (look for the help manual)
    # then return a random integer from [0,1]
    # if the return integer is 0, return 'computer'
    # else return 'player'
    r = random.randrange(0, 2)
    return 'computer' if r==0 else 'player'

def playAgain():
    """This function returns True if the player wants to play again, 
    otherwise it returns False"""
    print('Do you want to play again?(yes or no)')
    return True if input().lower() == 'y' else False

def makeMove(board,letter,move):
    """This function adds the player's move to the board"""
    board[move] = letter

def isWinner(board,letter):
    """
    Given a board and a player's letter, 
    this function returns True if the player has won. 
    """
    # 横线
    for i in [1, 4, 7]:
        if board[i]==board[i+1]==board[i+2]==letter:
            return True
    # 竖线
    for i in [1, 2, 3]:
        if board[i]==board[i+3]==board[i+6]==letter:
            return True
    # 斜线
    if board[3]==board[5]==board[7]==letter:
        return True
    if board[1]==board[5]==board[9]==letter:
        return True
    return False

def isSpaceFree(board,move):
    """Return True if the passed move is free on the passed board"""
    return True if board[move] == ' ' else False

import string
def getPlayerMove(board):
    """Let the player type in their move."""
    # ask the player to input their move
    # until int(move) is a number between 1 to 9 and the move is free on board
    # then return move as a number
    while True:
        move = input('what is your next move?(1-9)\n')
        if move in string.digits and len(move) == 1 and isSpaceFree(board, int(move)):
            break
        print('please choose a free place(1-9)!')
    return int(move)

def chooseRandomMoveFromList(board,movesList):
    """
    Returns a valid move from the passed list on the passed baord.
    Returns None if there is no valid move"""
    possibleMoves = []
    # for each move in movesList, 
    # if the move is free on board,
    # then add the move to possibleMoves
    for move in movesList:
        if isSpaceFree(board, move):
            possibleMoves.append(move)
    # if the length of possibleMoves is not 0
    # then randomly choose one and return it
    # else renturn None
    return None if len(possibleMoves) == 0 else random.choice(possibleMoves)

def getComputerMove(board,computerLetter):
    """
    Given a board and the computer's letter, 
    determine where to move and return that move
    """
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    # Here is the algorithm for Tic Tac Toe AI:
    # first, check if computer can win in the next move.
    # for all the 9 positions, if the position is free, then make move;
    # if that move can make the computer win, then return the position.
    
    for move in range(1, 10):
        if isSpaceFree(board, move):
            makeMove(board, computerLetter, move)
            win = isWinner(board, computerLetter)
            makeMove(board, ' ', move)
            if win:
                return move
            
    # check if the player could win on their next move, and block them.
    # otherwise, return the position that makes the player win
    for move in range(1, 10):
        if isSpaceFree(board, move):
            makeMove(board, playerLetter, move)
            win = isWinner(board, playerLetter)
            makeMove(board, ' ', move)
            if win:
                return move
            
    # take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move
    # take the center, if it is free.
    if isSpaceFree(board,5):
        return 5
    # Move on one of the sides
    return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    """
    Return True if every space on the board has been taken. 
    Otherwise return False.
    """
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

# the main body of the Tic Tac Toe 
print('Welcome to Tic Tac Toe!')
while True:
    # reset the board
    theBoard =  [' '] * 10 
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player': # player's turn
            # print out the board
            drawBoard(theBoard)
            # get player's move, and set it to variable move
            playermove = getPlayerMove(theBoard)
            # adds the player's move to the board
            makeMove(theBoard, playerLetter, playermove)
            # if the player has won
            if isWinner(theBoard, playerLetter):
                # print out the board
                drawBoard(theBoard)
                # print the prompt message
                print("Hooray! You have won the game!")
                # set gameIsPlaying to False
                gameIsPlaying = False
            # else
            else:
                # if the board is full
                if isBoardFull(theBoard):
                    # print out the board
                    drawBoard(theBoard)
                    # print the prompt message "The game is a tie!"
                    print("The game is a tie!")
                    # end the loop
                    gameIsPlaying = False
                # else
                else:
                    # set turn to computer
                    turn = 'computer'
        else:
            # computer's turn
            # get the computer move
            computermove = getComputerMove(theBoard, computerLetter)
            #  adds the computer's move to the board
            makeMove(theBoard, computerLetter, computermove)
            # if the computer has won
            if isWinner(theBoard, computerLetter):
                # print out the board
                drawBoard(theBoard)
                # print the prompt message
                print("The computer has beaten you! You lose.")
                # set gameIsPlaying to False
                gameIsPlaying = False
            # else
            else:
                # if the board is full
                if isBoardFull(theBoard):
                    # print out the board
                    drawBoard(theBoard)
                    # print the prompt message "The game is a tie!"
                    print("The game is a tie!")
                    # end the loop
                    gameIsPlaying = False
                # else
                else:
                    # set turn to player.
                    turn = 'player' 
    if not playAgain():
        break 
