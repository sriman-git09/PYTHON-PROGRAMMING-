
# Tic-tac-toe game in python 
# Human is X, computer is O. 
# Remember: minimax is a bit slow on the first move sometimes, but it works lol.

# Global board list, maybe should have used a class but whatever, this is fine for a simple script
theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def printBoard():
    # just printing the board manually cause it's easier than looping sometimes
    print()
    print(theBoard[0] + ' | ' + theBoard[1] + ' | ' + theBoard[2])
    print('--+---+--')
    print(theBoard[3] + ' | ' + theBoard[4] + ' | ' + theBoard[5])
    print('--+---+--')
    print(theBoard[6] + ' | ' + theBoard[7] + ' | ' + theBoard[8])
    print()

def isWinner(p):
    # checking all possible win conditions manually 
    # TODO: make this shorter later? nah, it works fine
    if (theBoard[0] == p and theBoard[1] == p and theBoard[2] == p) or \
       (theBoard[3] == p and theBoard[4] == p and theBoard[5] == p) or \
       (theBoard[6] == p and theBoard[7] == p and theBoard[8] == p) or \
       (theBoard[0] == p and theBoard[3] == p and theBoard[6] == p) or \
       (theBoard[1] == p and theBoard[4] == p and theBoard[7] == p) or \
       (theBoard[2] == p and theBoard[5] == p and theBoard[8] == p) or \
       (theBoard[0] == p and theBoard[4] == p and theBoard[8] == p) or \
       (theBoard[2] == p and theBoard[4] == p and theBoard[6] == p):
        return True
    return False

def checkTie():
    if ' ' not in theBoard:
        return True
    return False

def playerTurn():
    while True:
        try:
            spot = int(input("Pick a spot 1-9: ")) - 1
            if spot >= 0 and spot <= 8:
                if theBoard[spot] == ' ':
                    theBoard[spot] = 'X'
                    break
                else:
                    print("Hey, that spot is already taken!")
            else:
                print("I said between 1 and 9 bro.")
        except ValueError:
            print("Please just type a number.")

# minimax function - took me a while to get this recursion right 
def minimax(depth, isMax):
    if isWinner('O'):
        return 1
    if isWinner('X'):
        return -1
    if checkTie():
        return 0

    if isMax:
        bestScore = -999 # infinity basically
        for i in range(len(theBoard)):
            if theBoard[i] == ' ':
                theBoard[i] = 'O'
                score = minimax(depth + 1, False)
                theBoard[i] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 999
        for i in range(len(theBoard)):
            if theBoard[i] == ' ':
                theBoard[i] = 'X'
                score = minimax(depth + 1, True)
                theBoard[i] = ' '
                bestScore = min(score, bestScore)
        return bestScore

def aiTurn():
    bestScore = -999
    bestMove = 0
    
    for i in range(9):
        if theBoard[i] == ' ':
            theBoard[i] = 'O'
            score = minimax(0, False)
            theBoard[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
                
    theBoard[bestMove] = 'O'

# Game loop starts here
print("Welcome to Tic Tac Toe!")
printBoard()

while True:
    playerTurn()
    printBoard()
    
    if isWinner('X'):
        print("You actually won??? Nice.")
        break
    if checkTie():
        print("It's a tie game.")
        break
        
    print("AI is thinking...")
    aiTurn()
    printBoard()
    
    if isWinner('O'):
        print("Ha! AI wins. Git gud.")
        break
    if checkTie():
        print("Tie game.")
        break
