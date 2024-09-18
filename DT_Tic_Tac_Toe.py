'''
Pseudcode:
1. Initialize an empty board every time a new game starts
2. print the empty board to the user
3. iterate the plays for 9 times since we know there can be no more plays for a particular game
4. first is player X and once an iteration completed swap between player between O and X
5. Get the input from the user for each play and validate the input.
    If value<0 or >2 print error message
6. If values are correct check if the spot is open to play by checking if the row and column in the board is empty
7. Place X or O in the selected spot and check for winning
8. We check only 3 parts
    a. the row in which the insert happened (not necessary to check other rows)
    6. the column in which the insert happened
    c. If both the row and column values are equal check the first diagonal
    b. if adding both row and column gives 2(n-1) check the opposite diagonal
7. If none of the above check results in full 3 count for X or O return False. Else return the winner and jump to step-10
8. Print the winner if the returned value is true else continue by repeating steps (5-7)
9. If all the 9 plays are done, Print Draw match
10. Ask for a new game if yes repeat from step(1-10)
'''


class TicTacToe:
    def __init__(self):
        #initialize an empty board everytime a new game starts
        self.board = [['','',''],['','',''],['','','']]
    def print_board(self):
        #board constants that that doesnt change for each play
        print('-------------------')
        print('| R\C | 0 | 1 | 2 |')
        print('-------------------')
        #print the values stored in board for each game
        for i in range(3):
            print('| '+str(i).ljust(3),end = ' | ')
            for j in range(3):
                if(self.board[i][j]==''): #if empty spot print empty space
                    print(' ',end = ' | ') 
                else:
                    print(self.board[i][j],end = ' | ')
            print()
            print('-------------------')
        return 
    
    def Get_checkavailability(self):
        available = False # Initially availability is false
        while(not(available)):
            r,c = map(int,input('Please enter row number and column number separated by a comma.').split(','))
            while(r<0 or r>2 or c<0 or c>2): # If incorrect values provided get input
                print('Invalid entry: try again.')
                print('Row & column numbers must be either 0, 1, or 2.')
                r,c = map(int,input('Please enter row number and column number separated by a comma.').split(','))
            # check if the space is occupied
            if(self.board[r][c]!=''):
                available = False
            else:
                available = True
            if(not(available)):
                print('That cell is already taken.')
                print('Please make another selection.')
        #if all tests are passed display the input
        print('You have entered row #'+str(r))
        print('\t\t and column #'+str(c))
        return (r,c)
        
    def __checkcomplete(self,pointer,flag,player):
        #if flag is r check the particular row for the count of the player
        if(flag=='r'):
            if(self.board[pointer].count(player)==3):
                return True
            return False
        #if flag is 'c' check the particular column for the count of the player
        if(flag=='c'):
            for i in range(3):
                if(self.board[i][pointer]!=player):
                    return False
            return True
        #if the flag is 'd' check the diagonals for the count of the player
        if(flag=='d'):
            if(pointer==0):#for 1st diagonal
                for i in range(3):
                    if(self.board[i][i]!=player):
                        return False
                return True
            else:#for opposite diagonal
                for i in range(3):
                    if(self.board[2-i][i]!=player):
                        return False
                return True
                    
    def fill_checkwin(self,r,c,player):
        self.board[r][c] = player #place the current player in the board
        res = self.__checkcomplete(r,'r',player) # check for row match
        if(res==True):
            return player + ' is the Winner!!!'
        res = self.__checkcomplete(c,'c',player) # check for column match
        if(res==True):
            return player + ' is the Winner!!!'
        if(r==c): # check for first diagonal match
            res = self.__checkcomplete(0,'d',player)
            if(res==True):
                return player + ' is the Winner!!!'
        if((r+c)==(2)): #check for opposite diagonal match
            res = self.__checkcomplete(1,'d',player)
            if(res==True):
                return player + ' is the Winner!!!'
        return

def main():
    choice = 'y'
    while(choice.lower() in ('y','yes')):
        new_game = TicTacToe() #Initialize a new game
        print('New Game: X goes first.')
        new_game.print_board()
        player = 'X'
        Complete = 0
        for i in range(9): # each game consist of 9 plays
            print(player+"'s turn.")
            print('Where do you want your '+ player +' placed?')
            r,c = new_game.Get_checkavailability() # get input from user and validate the input
            print('Thank you for your selection.')
            result = new_game.fill_checkwin(r,c,player) # fill the selection and check for win
            if(result != None):#if there is a win print the winner and break the play
                print(result)
                new_game.print_board()
                Complete = 1
                break
            #swap the player after each turn
            if(player=='O'):
                player = 'X'
            else:
                player = 'O'
            if(i < 8): #print the board only 8 times since the last play print is happening outside
                new_game.print_board()
        if(Complete==0): #if there is no winner print the board
            print('Draw! NOBODY WINS!')
            new_game.print_board()
        #ask the user for a new game
        choice = input('Another game? Enter Y or y for yes.')
    print('Thank you for Playing!')

main()