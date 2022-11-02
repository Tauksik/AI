import random

board = [' ' for x in range(10)]


def displayBoard():
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |')


def makeMove(letter, pos):
    global board
    board[pos] = letter


def isFree(pos):
    return board[pos] == ' '


def notFull(board):
    return board.count(' ') > 1


def isWinner(board, ch):
    return ((board[7] == ch and board[8] == ch and board[9] == ch) or
            (board[4] == ch and board[5] == ch and board[6] == ch) or
            (board[1] == ch and board[2] == ch and board[3] == ch) or
            (board[7] == ch and board[4] == ch and board[1] == ch) or
            (board[8] == ch and board[5] == ch and board[2] == ch) or
            (board[9] == ch and board[6] == ch and board[3] == ch) or
            (board[7] == ch and board[5] == ch and board[3] == ch) or
            (board[9] == ch and board[5] == ch and board[1] == ch))


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if cornersOpen:
        move = random.sample(cornersOpen, 1)[0]
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if edgesOpen:
        move = random.sample(edgesOpen, 1)[0]
    return move


def main():
    print('Coputer vs Computer tictactoe program')
    displayBoard()

    while notFull(board):
        move = compMove()
        if not move:
            print('Tie!!! No more spaces left to move')
        else:
            makeMove('X', move)
            print(f'Computer1 placed \'X\' in position {move}')
            displayBoard()

        if isWinner(board, 'X'):
            print('Computer1 won')
            break

        move = compMove()
        if not move:
            print('It is a tie')
            return
        else:
            makeMove('O', move)
            print(f'Computer2 placed \'O\' in position {move}')
            displayBoard()

        if isWinner(board, 'O'):
            print('Computer2 wins')
            break

    if not notFull(board):
        print('It is a tie')


main()
