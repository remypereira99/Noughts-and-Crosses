board = [' ','_',' ','_',' ','_','\n','|','_','|','_','|','_','|','\n','|','_','|','_','|','_','|','\n','|','_','|','_','|','_','|']

def reset_board():
   
    global board
    
    board = [' ','_',' ','_',' ','_','\n','|','_','|','_','|','_','|','\n','|','_','|','_','|','_','|','\n','|','_','|','_','|','_','|']

def display():

    print(''.join(board))   
def display_label():
     
    labelled_board = ''.join([' ','_',' ','_',' ','_','\n','|','1','|','2','|','3','|','\n','|','4','|','5','|','6','|','\n','|','7','|','8','|','9','|'])
    
    print(labelled_board)    
def xo_choice():
    
    #Allows players to choose to be either X or O
    
    print('\nWelcome to Noughts and Crosses!\n')
    
    player_choice = 'N/A'
    
    while player_choice not in ['O','X']:
        
        player_choice = input('Would you like to be X or O?').upper()
        
        if player_choice not in ['O','X']:
            print('\nOops! You must choose either X or O. Please try again.\n')
            continue

        if player_choice=='X':
            print('\nYou will be Player 1')
            break
            
        if player_choice=='O':
            print('\nYou will be Player 2')
            break   
def player_1():

    turn = 'N/A'

    while turn not in range(0,10):

        turn = input('\nPlayer 1, choose a number from 1-9 to place your X on: ')

        try:
            int_turn = int(turn)
        except ValueError:
            print('\nInvalid move! Please try again.')
            player_1()

        if int_turn in range(0,4):

            if board[(int_turn*2)+6] in ['X','O']:
                print('\nPlace already taken! Please try again.\n')
                display()
                player_1()
                
            else:
                board[(int_turn*2)+6] = 'X'
                display()
                win_cond()
                break
            
        elif int_turn in range(4,7):
            if board[(int_turn*2)+8] in ['X','O']:
                print('\nPlace already taken! Please try again.\n')
                display()
                player_1()
            else:
                board[(int_turn*2)+8] = 'X'
                display()
                win_cond()
                break
            
        elif int_turn in range(7,10):
            if board[(int_turn*2)+10] in ['X','O']:
                print('\nPlace already taken! Please try again.\n')
                display()
                player_1()
            else:
                board[(int_turn*2)+10] = 'X'
                display()
                win_cond()
                break
def player_2():
    
    turn = 'N/A'
    
    while turn not in range(0,10):
        
        turn = input('\nPlayer 2, choose a number from 1-9 to place your O on: ')
        
        try:
            int_turn = int(turn)
        except ValueError:
            print('\nInvalid move! Please try again.')
            player_2()
        
        int_turn = int(turn)
        
        if int_turn in range(0,4):
            if board[(int_turn*2)+6] in ['X','O']:
                print('\nPlace already taken! Please try again.\n')
                display()
                player_2()
            else:
                board[(int_turn*2)+6] = 'O'
                display()
                win_cond()
                break
            
        elif int_turn in range(4,7):
            if board[(int_turn*2)+8] in ['X','O']:
                print('\nPlace already taken! Please try again.\n')
                display()
                player_2()
            else:
                board[(int_turn*2)+8] = 'O'
                display()
                win_cond()
                break
            
        elif int_turn in range(7,10):
            if board[(int_turn*2)+10] in ['X','O']:
                print('\nPlace already taken! Please try again.\n')
                display()
                player_2()
            else:
                board[(int_turn*2)+10] = 'O'
                display()
                win_cond()
                break
        
def win_cond():

    x_cnt = 0
    o_cnt = 0
    end_game = 0

    row1 = [board[8],board[10],board[12]]
    row2 = [board[16],board[18],board[20]]
    row3 = [board[24],board[26],board[28]]
    column1 = [board[8],board[16],board[24]]
    column2 = [board[10],board[18],board[26]]
    column3 = [board[12],board[20],board[28]]
    diagonal1 = [board[8],board[18],board[28]]
    diagonal2 = [board[12],board[18],board[24]]

    all_poss = [row1,row2,row3,column1,column2,column3,diagonal1,diagonal2]
    
    rows = [board[8],board[10],board[12],board[16],board[18],board[20],board[24],board[26],board[28]]

    for lst in all_poss:
        if lst.count('X')==3:
            end_game=1
            print('\nCongratulations, Player 1 wins!'.upper())
            play_again()
        elif lst.count('O')==3:
            end_game=1
            print('\nCongratulations, Player 2 wins!'.upper())
            play_again()
            
    if rows.count('_')==0:
        print("\nIt's a draw!")
        play_again()
    
    if end_game==0:
        if rows.count('_')>0:
            for row in rows:
                if 'X' in row:
                    x_cnt+=1
                if 'O' in row:
                    o_cnt+=1
            if x_cnt>o_cnt:
                player_2()
            elif x_cnt==o_cnt:
                player_1()
def play_again():
    
    answer = 'N/A'
    
    while answer not in ['yes','no','y','n']:
        
        answer = input('\nWould you like to play again?\n').lower()
        
        if answer== 'yes' or answer=='y':
            game_program()
        
        if answer== 'no' or answer=='n':
            print('\nThanks for playing!')
def game_program():
    
    reset_board()
    
    xo_choice()
    
    display_label()
    
    player_1()

if __name__ == '__main__':
    game_program()
