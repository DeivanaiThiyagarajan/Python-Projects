class Connect_Four:
    def __init__(self):
        self.board = [['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
        self.num_alpha_dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
        self.aplha_num_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
        #self.first_set_diagonals = [['a3','b4','c5','d6'],['a2','b3','c4','d5','e6'],['a1','b2','c3','d4','e5','f6'],['b1','c2','d3','e4','f5','g6'],['c1','d2','e3','f4','g5'],['d1','e2','f3','g4']]
        #self.opposite_set_diagonals = {3:['30','21','12','03'],4:['40','31','22','13','04'],5:['50','41','32','23','14','05'],6:['51','42','33','24','15','06'],7:['52','43','34','25','16'],8:['53','44','35','26']}
    def print_board(self):
        print('---------------------------------')
        for i in range(6,0,-1):
            print('| '+ str(i),end=' | ')
            for j in range(7):
                if(self.board[i-1][j]==''):
                    print(' ',end = ' | ')
                else:
                    print(self.board[i-1][j],end=' | ')
            print()
            print('---------------------------------')
        print('|R/C| a | b | c | d | e | f | g |')
        print('---------------------------------')
    def available_positions(self):
        l = []
        #alpha_num_dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
        for i in range(7):
            for j in range(6):
                if(self.board[j][i]==''):
                    l.append(self.num_alpha_dict[i+1]+str(j+1))
                    break
        return l
    def check_move(self,move,available):
        if(move[0] not in ('a','b','c','d','e','f','g') or move[1] not in ('1','2','3','4','5','6')):
            return 'incorrect'
        elif(move not in available):
            return 'unavailable'
        else:
            return 'correct'
        
    def play_move(self,move,player):
        column = self.aplha_num_dict[move[0]]-1
        row = int(move[1])-1
        #print(number)
        self.board[row][column] = player
        return
    
    def __validate(self,listofRecords,player):
        count = 0
        for i in listofRecords:
            if(i==player):
                count+=1
                if(count==4):
                    return True
            else:
                count = 0
        if(count==4):
            return True
        return False
    
    def validate_move(self,move,player):
        column = self.aplha_num_dict[move[0]]-1
        row = int(move[1])-1
        listrow = self.board[row]
        result = self.__validate(listrow,player)
        if(result == True):
            return player + ' is the Winner!'
        if(row>2):
            listcolumn = []
            for i in range(6):
                listcolumn.append(self.board[i][column])
            result = self.__validate(listcolumn,player)
            if(result == True):
                return player + ' is the Winner!'
            
            listdiagonal1 = []
            i=row
            j=column
            while(i>=0 and j>=0):
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
            while(i>=0 and j<=6):
                listdiagonal2.append(self.board[i][j])
                i-=1
                j+=1
            if(len(listdiagonal2)>3):
                result = self.__validate(listdiagonal2,player)
                if(result == True):
                    return player + ' is the Winner!'
        return None
            
        

def main():
    choice = 'y'
    while(choice.lower() in ('y','yes')):
        print('New game: X goes first.')
        new_game = Connect_Four()
        new_game.print_board()
        player = 'X'
        complete = False
        for i in range(42):
            print(player+"'s turn.")
            print('Where do you want your '+player+' placed?')
            available = new_game.available_positions()
            print('Available positions are:',available)
            print()
            incorrect_move = True
            while(incorrect_move):
                move = input('Please enter column-letter and row-number (e.g., a1):')
                check_move = new_game.check_move(move,available)
                if(check_move=='incorrect'):
                    print('Invalid entry: try again.')
                elif(check_move == 'unavailable'):
                    print('That cell is already taken.')
                    print('Please make another selection.')
                else:
                    incorrect_move = False
            new_game.play_move(move,player)
            if(i>5):
                result = new_game.validate_move(move,player)
                if(result != None):
                    print(result)
                    complete = True
                    new_game.print_board()
                    break
            if(player == 'X'):
                player = 'O'
            else:
                player = 'X'
            if(i<42):
                new_game.print_board()
        if(complete==0): #if there is no winner print the board
            print('Draw! NOBODY WINS!')
            new_game.print_board()
        choice = input('Another game (y/n)?')
    print('Thank you for playing!')

main()