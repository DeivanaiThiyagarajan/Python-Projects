'''
Pseudcode:
1. Initialize an empty board every time a new game starts
2. print the empty board to the user
3. iterate the plays for 42 times since we know there can be no more plays for a particular game
4. first is player X and once an iteration completed swap between player between O and X
5. Get a list of available positions in the board currently
6. Get the input from the user for each play and validate the input.
    If the input is not in the available list print error message and ask the user to enter the input again
7. If values are correct check if the spot is open to play by checking if the row and column in the board is empty
8. Place X or O in the selected spot and check for winning
    - to find the correct spot check the column value and row value
    - compare the column value with the number in the board array using Alpha_num_dict
    - place the player in the column row value found
9. For checking We check only 3 parts
    a. the row in which the insert happened (not necessary to check other rows)
    6. the column in which the insert happened (This check needs to happen if only the row value is greater than 2)
    c. check the off diagonal for consecutive 4 same characters by decrementing row and column value by 1
    b. check the main diagonal for the same by decrementing row value and incrementing column value
10. If none of the above check results in full 4 count for X or O return False. Else return the winner and jump to step-13
11. Print the winner if the returned value is true else continue by repeating steps (5-10)
12. If all the 42 plays are done, Print Draw match
13. Ask for a new game if yes repeat from step(1-12)
'''

class Connect_Four:
    def __init__(self): # Initialize a new board whenever a new game is requested
        self.board = [['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
        #num-alpha dictionary to map number to column alphabet
        self.num_alpha_dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'} 
        # alpha-num dictionary to convert alphabet to number to access the list (board)
        self.aplha_num_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
    def print_board(self):
        # print the board values
        print('---------------------------------')
        for i in range(6,0,-1):
            print('| '+ str(i),end=' | ')
            for j in range(7):
                if(self.board[i-1][j]==''): #check for empty spot
                    print(' ',end = ' | ') 
                else:
                    print(self.board[i-1][j],end=' | ')
            print()
            print('---------------------------------')
        # print the board constants
        print('|R/C| a | b | c | d | e | f | g |')
        print('---------------------------------')
    def available_positions(self):
        #once the function is called check the currently available positions in the board
        l = []
        for i in range(7): #check for all columns
            for j in range(6):
                if(self.board[j][i]==''):
                    l.append(self.num_alpha_dict[i+1]+str(j+1))
                    break #break searching the other rows if eg: 0 spot is empty for a column
        return l
    def check_move(self,move,available):
        #check if the move is correct by checking if the first character input is between a-g
        #check if the second character is between 1-6
        if(len(move)!=2 or move[0] not in ('a','b','c','d','e','f','g') or move[1] not in ('1','2','3','4','5','6')):
            return 'incorrect'
        elif(move not in available): # check if the spot is available list
            return 'unavailable'
        else: #return as correct move
            return 'correct'
        
    def play_move(self,move,player):
        #Find the column numeric index by using the alpha_num_dictionary
        column = self.aplha_num_dict[move[0]]-1
        #subtract nrow number input by -1 since the input user enters is 1-indexed but list is 0-indexed
        row = int(move[1])-1
        #place the player in the respective row an column in the board
        self.board[row][column] = player
        return
    
    def __validate(self,listofRecords,player):
        count = 0
        for i in listofRecords: #get the current list to check
            if(i==player):
                count+=1
                if(count==4): #check if the count is 4 if so return true for winner
                    return True
            else:
                count = 0 #assign count to 0 if any inbetween value is another player
        if(count==4):
            return True #if count reaches four return true else false
        return False
    
    def validate_move(self,move,player):
        #Find the column numeric index by using the alpha_num_dictionary
        column = self.aplha_num_dict[move[0]]-1
        #subtract nrow number input by -1 since the input user enters is 1-indexed but list is 0-indexed
        row = int(move[1])-1
        listrow = self.board[row] 
        #check the current column that the user has placed his move in
        result = self.__validate(listrow,player)
        if(result == True):
            return player + ' is the Winner!'
        if(row>2): #check for column and dioagonal winner only if the row is greater than 2
            listcolumn = []
            for i in range(6): #check the current column
                listcolumn.append(self.board[i][column])
            result = self.__validate(listcolumn,player)
            if(result == True):
                return player + ' is the Winner!'
            
            listdiagonal1 = []
            i=row
            j=column
            while(i>=0 and j>=0): # check the off-diagonal
                listdiagonal1.append(self.board[i][j])
                i-=1
                j-=1
            if(len(listdiagonal1)>3):
                result = self.__validate(listdiagonal1,player)
                if(result == True):
                    return player + ' is the Winner!'
            listdiagonal2=[]
            i=row
            j=column
            while(i>=0 and j<=6): # check the main diagonal
                listdiagonal2.append(self.board[i][j])
                i-=1
                j+=1
            if(len(listdiagonal2)>3):
                result = self.__validate(listdiagonal2,player)
                if(result == True):
                    return player + ' is the Winner!'
        return None
            
        

def main():
    choice = 'y' # Initial choice is yes for atleast one game in the start
    while(choice.lower() in ('y','yes')):
        print('New game: X goes first.')
        new_game = Connect_Four() #Initialize the board
        new_game.print_board() # print the empty board to the user to ask input
        player = 'X'
        complete = False
        for i in range(42):
            print(player+"'s turn.")
            print('Where do you want your '+player+' placed?')
            available = new_game.available_positions() #get the list of available positions
            print('Available positions are:',available)
            print()
            incorrect_move = True #initiallt incorrect move is true to get the input
            while(incorrect_move):
                move = input('Please enter column-letter and row-number (e.g., a1):')
                check_move = new_game.check_move(move,available) #check the move of the player
                if(check_move=='incorrect'): #print error message if incorrect move and ask the new input again
                    print('Invalid entry: try again.')
                elif(check_move == 'unavailable'): #print error message if move not available and ask for new input
                    print('That cell is already taken.')
                    print('Please make another selection.')
                else:
                    incorrect_move = False
            new_game.play_move(move,player) #place the player in the position mentioned
            if(i>5): #check if atleast 5 moves passed as there cannot be winner less than 5 moves
                result = new_game.validate_move(move,player) #validate the move for winner
                if(result != None): #if result is not none then there is a winner print the message
                    print(result)
                    complete = True # set complete to true to end the game
                    new_game.print_board() #print the final board
                    break #break this game
            if(player == 'X'): #swap between the players
                player = 'O'
            else:
                player = 'X'
            if(i<42):
                new_game.print_board() #if current turn is less than 42 print the current state of the board
        if(complete==0): #if there is no winner print the board and display draw game message
            print('Draw! NOBODY WINS!')
            new_game.print_board()
        choice = input('Another game (y/n)?') #Ask the user for a new game
    print('Thank you for playing!')

if __name__ == '__main__':
    main()