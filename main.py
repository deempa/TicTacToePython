import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

HEIGHT = 3
WIDTH = 3
SEQUENCE_NEED = 3
X = 'X'
O = 'O'


def main():
    welcome()
    board = boardInit(HEIGHT, WIDTH)
    player1 = X
    player2 = O
    who_is_turn = player1
    printBoard(board)
    while True:
        print()
        print("Current player : " + who_is_turn)
        print()
        player_choice = input("Move > ")
        while not player_choice.isdecimal():
            print("Wrong input or place is already taken.")
            player_choice = input("Move > ")
        player_choice = int(player_choice)

        while not placeIsValid(board, player_choice // HEIGHT, player_choice % WIDTH):
            print("Wrong input or place is already taken.")
            player_choice = input("Move > ")
            while not player_choice.isdecimal():
                print("Wrong input or place is already taken.")
                player_choice = input("Move > ")

            player_choice = int(player_choice)

        welcome()

        updateBoard(board, player_choice // HEIGHT, player_choice % WIDTH, who_is_turn)

        # Check if someone won after the last move
        if checkIfWin(board, player_choice // HEIGHT, player_choice % WIDTH, who_is_turn):
            welcome()
            printBoard(board)
            print(Back.WHITE + Fore.BLACK + "\nThe winner is %s ! " % who_is_turn)
            goodBye()
            break

        # Check if Tie
        if boardIsFull(board):
            print("Tie Game! ")
            goodBye()
            break

        # Change the turn for the next player
        who_is_turn = switchTurn(who_is_turn, player1, player2)


def boardInit(width, height):
    return [["%d" % (x * HEIGHT + y) for y in range(width)] for x in range(height)]


def printBoard(board):
    for i in range(HEIGHT):
        print("%10s" % "", end="")
        for j in range(WIDTH):
            if j == WIDTH - 1:
                print("%3s" % board[i][j], end="")
            else:
                print("%3s   | " % board[i][j], end="")
        print()


def updateBoard(board, x, y, symbol):
    board[x][y] = symbol
    printBoard(board)


def placeIsValid(board, x, y):
    if x < 0 or y < 0 or x >= HEIGHT or y >= WIDTH:
        return False
    if board[x][y] == X or board[x][y] == O:
        return False
    return True


def checkIfWin(board, x, y, symbol):
    if checkIfRowWin(board, x, symbol) or checkIfColWin(board, y, symbol) or checkIfLeftDiagonalWin(board, x, y, symbol) or checkIfRightDiagonalWin(board, x, y, symbol):
        return True
    return False


def checkIfRowWin(board, x, symbol):
    sequence = 0
    for col in range(WIDTH):
        if board[x][col] == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfColWin(board, y, symbol):
    sequence = 0
    for row in range(HEIGHT):
        if board[row][y] == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfLeftDiagonalWin(board, x, y, symbol):
    sequence = 0
    if x > y:
        x -= y
        y -= y
    elif x < y:
        y -= x
        x -= x
    else:
        x -= x
        y -= y

    while x < HEIGHT and y < WIDTH:
        if board[x][y] == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
        x += 1
        y += 1
    return False


def checkIfRightDiagonalWin(board, x, y, symbol):
    x, y = y, x
    sequence = 0
    while x < HEIGHT and y < WIDTH:
        if board[y][x] == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
        x += 1
        y -= 1
    return False


def boardIsFull(board):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] != X and board[i][j] != O:
                return False
    return True


def switchTurn(who_is_turn, player1, player2):
    if who_is_turn == player1:
        return player2
    return player1


def welcome():
    os.system("clear")
    print(Back.GREEN + Fore.BLACK + " WELCOME TO THE GAME OF TIC-TAC-TEO \n")


def goodBye():
    print("\nThanks for playing my TIC-TAC-TEO game!")
    print("See you next time.\n")


if __name__ == '__main__':
    main()
