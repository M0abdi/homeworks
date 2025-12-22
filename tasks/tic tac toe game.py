
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_win():
    # rows
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    
    # columns
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    
    # diagonals
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    
    return False

# start
print("Welcome to Tic Tac Toe!")
print(" ")
print("First player is X, second is O")
print("")
print("Enter a number 1-9 to place your mark")

player = "X"


for turn in range(9):
    show_board()
    
    
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9")
            elif board[move] == "X" or board[move] == "O":
                print("That spot is already taken!")
            else:
                break
        except:
            print("Please enter a valid number")
    
    
    board[move] = player
    
    
    if check_win():
        show_board()
        print(f"Player {player} wins! :] ")
        break
    
    
    if player == "X":
        player = "O"
    else:
        player = "X"
else:
    
    show_board()
    print("It's a tie! :0  ")
