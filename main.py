#---------global variable---------#

print("********************Let's play TIC - TAC - TOE !!!!!******************")
#board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going on:
game_still_going = True

# Who won? Or tie?
winner = None

#Who's turn is it?
current_player = 'X'

#displayboard
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#play a game of TIC-TAC-TOE!!!
def play_game():
    #display initial board
    display_board()

    # While the game is on:
    while game_still_going:

        #handle a single turn of an arbitary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #Flip to the other player
        flip_player()
    
    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner +  'won!')
    elif winner == None:
        print("It's a Tie!!")


# Handle a single turn of an arbitary player
def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input("Invalid input ! Choose a position from 1-9 : ")

        position = int(position)-1

        if board[position] == '-':
            valid = True
        else:
            print("You can't go there . Go again!")

    board[position]= player
    display_board()

def check_if_game_over():
    check_for_winnner()
    check_if_tie()

def check_for_winnner():

    #set up global variable
    global winner

    #check rows
    row_winner = check_rows()
    #check coloumns
    coloumn_winner = check_coloumns()
    #check diagonals
    diagonals_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return

def check_rows():
    #set up global varible
    global game_still_going
    # check if all values in the row are equal
    row_1 = board[0]==board[1]==board[2] != "-"
    row_2 = board[3]==board[4]==board[5] != "-"
    row_3 = board[6]==board[7]==board[8] != "-"
    #if any row does have  a match , declare it winner
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return a winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_coloumns():
    #set up global varible
    global game_still_going
    # check if all values in the row are equal
    col_1 = board[0]==board[3]==board[6] != "-"
    col_2 = board[1]==board[4]==board[7] != "-"
    col_3 = board[2]==board[5]==board[8] != "-"
    #if any row does have  a match , declare it winner
    if col_1 or col_2 or col_3:
        game_still_going = False
    #return a winner (X or O)
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diagonals():
    #set up global varible
    global game_still_going
    # check if all values in the row are equal
    diag_1 = board[0]==board[4]==board[8] != "-"
    diag_2 = board[6]==board[4]==board[2] != "-"
    #if any row does have  a match , declare it winner
    if diag_1 or diag_2 :
        game_still_going = False
    #return a winner (X or O)
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()


