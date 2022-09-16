from Player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board=self.make_board #we use a single list to represent 3*3
        self.current_winner=None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range (3)]: #0,1,2,3,4,5,6,7,8 for each square
            print ('|   '+'|   '.join(row)+'|   ')

    @staticmethod
    def print_board_num():
        number_board=[[str(i) for i in range ((j*3), ((j+1)*3))] for j in range (3)]
        for row in number_board:
            print ('|   '+'|   '.join(row)+'|   ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot==' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    #def function to acc make a move
    def make_move(self, square, letter):
        if ' ' == self.board[square]:
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square, letter):
        #row
        row_ind=square//3
        row=self.board[row_ind*3:(row_ind+1)*3]
        if all(spot==letter for spot in row):
            return True

        #check colums
        col_ind=square%3
        col=[self.board[col_ind+i*3] for i in range (3)]
        if all(spot==letter for spot in col):
            return True

        #check Diag
        if square%2==0:
            diagnol1=[self.board[i] for i in [0,4,8]]
            if all(spot==letter for spot in diagnol1):
                return True
            diagnol2=[self.board[i] for i in [2,4,6]]
            if all(spot==letter for spot in diagnol2):
                return True

        return False
    
        

def play(game,x_player, o_player, print_game=True):
    if print_game:
        game.print_board_num

    letter='X'

    while game.empty_squares:
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if not game.make_move   (square, letter):
            continue
        if print_game:
            print(letter + f' makes a move to square {square}'.format(square))
            game.print_board()
            print(' ')

        if game.current_winner:
            if print_game:
                print("YAY!", letter, "has won")

        if letter=='X':
            letter=='O'
        else:
            lettter='X'

        time.sleep(1)

    if print_game:
        print("its a tie")


if __name__=='__main__' :
    x_player=HumanPlayer('X')
    o_player=RandomComputerPlayer('O')
    play(TicTacToe(),x_player,o_player, print_game=True)

                


    
        
            
