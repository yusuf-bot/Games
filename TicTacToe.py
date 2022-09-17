import random


class TICTACTOE:
    def __init__(self, letter):
        self.human = letter
        self.moves = []
        for x in range(0, 9):
            self.moves.append(x)
        self.last_move = None
        self.done_moves=[]
        self.dig = [0,4,8]

    def boardx(self):
        count=1
        for x in self.moves:
            if count // 3 == count / 3:
                print(f'{x}')
            else:
                print(f'{x}|', end='')
            count+=1

    def play(self):
        if self.human == 'X':
            hmove = int(input("Enter which place you want to put it in: "))
            if hmove > 9:
                print('error')
                quit()
            self.moves = self.moves[:hmove]+['X']+self.moves[hmove+1:]
            self.last_move = self.human
            self.done_moves.append(hmove)
            self.board()
            self.winner()
            cmove = random.choice(self.moves)
            while cmove == 'X' or cmove == 'O':
                cmove = random.choice(self.moves)
            print("The Computer played at: ",cmove)
            self.moves = self.moves[:cmove]+['O']+self.moves[cmove+1:]
            self.last_move = 'O'
            self.done_moves.append(cmove)
            self.board()
            self.winner()
        else:
            cmove = random.choice(self.moves)
            while cmove == 'X' or cmove == 'O':
                cmove = random.choice(self.moves)
            print("The Computer played at: ",cmove)
            self.last_move = 'X'
            self.moves = self.moves[:cmove] + ['X'] + self.moves[cmove + 1:]
            self.done_moves.append(cmove)
            self.board()
            self.winner()
            hmove = int(input("Enter which place you want to put it in: "))
            if hmove > 9:
                print('error')
                quit()
            self.moves = self.moves[:hmove]+['O']+self.moves[hmove+1:]
            self.last_move = self.human
            self.done_moves.append(hmove)
            self.board()
            self.winner()


    def board(self):
        count=1
        for x in self.moves:
            if x=='X' or x=='O':
                if count // 3 == count / 3:
                    print(f'{x}')
                else:
                    print(f'{x}|', end='')
            else:
                if count // 3 == count / 3:
                    print(' ')
                else:
                    print (' |',end='')

            count+=1
    def winner(self):
        if self.moves[0]==self.moves[4]==self.moves[8]:
            print (self.last_move,'won')
            quit()

        elif self.moves[2]==self.moves[4]==self.moves[6]:
            print (self.last_move,'won')
            quit()

        for x in range(0,3):
            if self.moves[x]==self.moves[x+3]==self.moves[x+6]:
                print (self.last_move,'won')
                quit()

        for x in range(0,7,3):
            if self.moves[x]==self.moves[x+1]==self.moves[x+2]:
                print (self.last_move,'won the game !!!')
                quit()


def games():
    game = TICTACTOE('X')
    game.boardx()
    while True:
        game.play()

games()
