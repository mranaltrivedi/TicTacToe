from IPython.display import clear_output
import random


#function that displays the board
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


#function that takes a valid user input/marker as either 'x' or 'o'
def player_input():
     
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Please select a valid marker.\n  Do you want an X or O? ").upper()
        
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')

#function that takes the user marker input and places it on a particular position on the board
def place_marker(board, marker, position):
    
    board[position] = marker


#funtion to check if that marker has won
def win_check(board, mark):
    
    #Create a dictionary of all possible winning combinations
    windict = {'123':{1,2,3},'456':{4,5,6},'789':{7,8,9},'147':{1,4,7},'258':{2,5,8},'369':{3,6,9},'159':{1,5,9},'357':{3,5,7}}
    
    #Run a for loop and user 'enumerate' to find all occurences of a marker and create a set out of them
    for key in windict.keys():
        for val in windict.values():
                
                #Check if the set of the board positions of any marker matches any of the winning combinations
                if val <= set([index for index, value in enumerate(board) if value.lower() == mark.lower()]):
                    return True
                    break
                else:
                    continue
    return False

#function that randomly decides which player goes first
def choose_first():
    num=random.randint(1,2)
    return num


#function that checks whether a position on the board is empty or not
def space_check(board, position):
    
    return board[position]==' '


#function that checks if the board is full or not
def full_board_check(board):
    
    for i in range(1,len(board)):
        if space_check(board,i):
            return False
    return True


#function that asks for the current player's next move
def player_choice(board):
    
    nextpos = 0
    while nextpos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,nextpos):
        nextpos = int(input('Please select the next position to place your marker(1-9): '))
    return nextpos


#function that asks the user if they want to keep on playing or not
def replay():
    
    return str(input('Do you want to play again? Enter Y/N! ')).lower() =='y'



#main game logic
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    #pass
    #Create an empty board
    your_board = [' ']*10
    
    #Set player markers
    player1_marker,player2_marker = player_input()
    
    #Pick which player goes first
    turn = choose_first()
    print(f'Player {turn} goes first!')
    
    #Ask user if they want to start playing
    play = input('Are you ready to play? y/n').lower()
    
    #Set the gameplay switch on or off
    if play=='y':
        game_on = True
    else:
        game_on = False
        
    #while loop for main game 
    while game_on:
    
        #Player 1 Turn
        if turn==1:
            #Display the board
            display_board(your_board)
            
            #Choose a position
            position = player_choice(your_board)
            
            #Place player's marker on that position
            place_marker(your_board, player1_marker, position)
            
            #Check if they won
            if win_check(your_board,player1_marker):
                display_board(your_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            
            else:
                #Since someone hasn't won yet, check for a tie by checking if the board is full
                if full_board_check(your_board):
                    display_board(your_board)
                    print('GAME IS TIED!!')
                    game_on = False
                else:
                    turn = 2
            
        
        # Player2's turn.
        else: 
            #Display the board
            display_board(your_board)
            
            #Choose a position
            position = player_choice(your_board)
            
            #Place player's marker on that position
            place_marker(your_board, player2_marker, position)
            
            #Check if they won
            if win_check(your_board,player2_marker):
                display_board(your_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            
            else:
                #Since someone hasn't won yet, check for a tie by checking if the board is full
                if full_board_check(your_board):
                    display_board(your_board)
                    print('GAME IS TIED!!')
                    game_on = False
                else:
                    turn = 1
            #pass

    #if not replay():
    if not replay():
        break
