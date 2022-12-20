import numpy as np
import random

def getInput(board):
    x = input('Enter row: ')
    y = input('Enter Column: ')
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return getInput(board)

    if (x < 0 or y < 0) or (x >2 or y >2) or (board[x][y] != ' '):
        # invalid input
        print('Error: Invalid Input')
        return getInput(board=board)
    return (x,y)

def computerInput(board):
    r = random.randint(0,2)
    c = random.randint(0,2)

    if board[r][c] != ' ':
        return computerInput(board=board)
    return (r,c)

def putPosition(board, x:int, y:int, player:int):
    board[x][y] = 'X' if player else 'O'

def checkRows(board):
    newBoard = board.transpose()

    for row in board:
        if (' ' not in row) and (len(set(row)) == 1):
            return row[0]

    for row in newBoard:
        if (' ' not in row) and (len(set(row)) == 1):
            return row[0]

    return ''

def printBoard(board):
    for row in board:
        print(row)


def checkDiagonal(board):
    diag = ''
    antiDiag = ''
    for i in range(len(board)):
        diag += board[i][i]
        antiDiag += board[i][-i + 2]
    
    if diag == 'XXX' or diag == 'OOO':
        return diag[0]
    elif antiDiag == 'XXX' or antiDiag == 'OOO':
        return antiDiag[0]
    else:
        return ''

def checkGame(board):
    rowValue = checkRows(board=board)
    if rowValue != '':
        return rowValue
    diagValue = checkDiagonal(board=board)
    if diagValue != '':
        return diagValue
    return 'Tie!'

def main():
    turn = 0
    board = np.array([[' ', ' ', ' '], [' ', ' ', ' '],[' ', ' ', ' ']])
    winner = 'Tie!'
    playerCheckVariable = random.randint(0,1)

    while (winner == 'Tie!' and turn < 9):
        if turn%2 == playerCheckVariable:
            # user
            r,c = getInput(board)
        else:
            # computer
            r,c = computerInput(board=board)
            print(f'Computer chose: ({r}, {c})')
        putPosition(board, r, c, turn%2)
        turn += 1
        printBoard(board)
        winner = checkGame(board=board)
    print(winner)

if __name__ == '__main__':
    main()