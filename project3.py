import random

def display(board):
    print(f"""
{board[7]}|{board[8]}|{board[9]}                         1 | 8 | 9
---+---+---                       --+---+---
{board[4]}|{board[5]}|{board[6]}     Positions -->       3 | 5 | 6
---+---+---                       --+---+---
{board[1]}|{board[2]}|{board[3]}                         7| 2 | 4
""")

def validInput():
    while True:
        pos = input("Enter your position: ")
        if pos != " ":
            if int(pos) in range(1,10):
                pos = int(pos)
                break
            print("Please enter valid position")
        else:
            print("Thank you for playing Tic-Tac-Toe!!!")
            exit()
    return int(pos)

def pos(turn, board):
    print(f'{turn} chance')
    pos = validInput()
    while True:
        if board[pos] == "   ":
            board[pos] = turn
            break
        else:
            print("Can't overwrite, please choose new location")
            pos = validInput()

def userInput(board, symbol):
    syml1, syml2 = symbol[random.randint(0, 1)]
    print(f"{syml1} is going first\n\n")
    display(board)
    for i in range(9):
        if i % 2 == 0:
            turn = " "+syml1+" "
            pos(turn, board)
        else:
            turn = " "+syml2+" "
            pos(turn, board)
        display(board)
        if i >= 4:
            if check(board):
                display(board)
                print(f"'{turn}' won the match")
                break
        if i == 8:
             print("No one won, tie match")

def check(board):
    check = 0
    if board[1] == board[2] == board[3] != "   " or board[4] == board[5] == board[6] or board[7] == board[8] == board[9]:
        check = 1
    elif board[4] == board[5] == board[6] != "   " or board[1] == board[2] == board[3] or board[7] == board[8] == board[9]:
        check = 1
    elif board[7] == board[8] == board[9] != "   " or board[1] == board[2] == board[3] or board[4] == board[5] == board[6]:
        check= 1
    return check

def playGame():
    board = ["Just to adjust location :", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ","   "]
    symbol = [("O", "X"), ("X", "O")]
    while True:
        marker = input("Choose your marker: ")
        if marker == "O" or marker == "X":
            userInput(board, symbol)
            break
        else:
            print("wrong marker(O, X) please choose again.\n")

def main():
    again = "y"
    while again == "y":
      print("Press {space} whenever you want to stop the game")
      playGame()
      again = input("Press 'y' to play again: ")
main() 
