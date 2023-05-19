import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
    pass

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    print("Welcome to the ' Noughts and Crosses' game.\nThe board looks as such:")
    draw_board(board)
    print("Please select from the options below how you would like to proceed\nIf you decide to play, please choose your move by entering one of the numbers indicated on the board")
    pass
  
def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for r in range(3):
        for c in range(3):
            board[r][c] = ' '
    
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        move = input('Above is the state of the board, enter the cell number where you want to place your move (1-9): ')
        print('After my move')
        try:
            cell = int(move)
            if cell in range(1, 10):
                row = (cell - 1) // 3
                col = (cell - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                print('Invalid position, position already occupied try again.')
            else:
                print('Invalid input, please select a number between 1-9 that is on the board.')
        except ValueError:
            print('Invalid entry.Are you sure you entered a number between 1-9')

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col

    # first establish the slots available for the computer to select randomly
    empty_spots = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_spots.append((row, col))

    # let the computer selct from that list
    if empty_spots:
        row, col = random.choice(empty_spots)
        print('After computer move')
        return row, col
    else:
        # no available spots
        return None
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise

    for row in board:
        if row == [mark, mark, mark]:
            return True
    for col in range(3):
        if board[0][col] == mark and board[1][col] == mark and board[2][col] == mark:
            return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False
  

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise

    for row in board:
        if ' ' in row:
            return False
    return True


    
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop

    while True:
        initialise_board(board)
        
        while True:
            draw_board(board)
            row, col = get_player_move(board)
            board[row][col] = 'X'
            draw_board(board)
            if check_for_win(board, 'X'):
                print('Congratulations, you have won!')
                return 1
          
            if check_for_draw(board):
                print('The game is a draw!')
                return 0
         

            row, col = choose_computer_move(board)
           
            board[row][col] = 'O'
            draw_board(board)
           
            if check_for_win(board, 'O'):
                print('Sorry, the computer has won!')
                return -1
            if check_for_draw(board):
                print('The game is a draw!')
                return 0
            play_again = input('Shall we go for another round? (y/n)')
            if play_again.lower() != 'y':
                break
        return 0
    return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program

    while True:
        print('1. Play')
        print('2. Save the game')
        print('3. Display leaderboard')
        print('q. Exit')
        choice = input('Please select what you want from the game:')
        return choice
    

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders

    scores = {}
    with open('leaderboard.txt', 'r') as f:
        data = f.read()
        leaders = eval(data)
    return leaders
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    
    scores = load_scores()

    # Ask the player for their name
    name = input("Enter your username: ")

    # Add the score to the leaderboard
    scores[name] = score

    # Save the updated leaderboard to the file
    with open('leaderboard.txt', 'w') as f:
        f.write(str(scores))


    
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader

    print('Current Top leaders in the game')
    print('-+-+-+-+-+-')
    for name, score in leaders.items():
        print(f'{name}: {score}')
    pass

