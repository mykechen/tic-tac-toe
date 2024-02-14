from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    # initializes game board 
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    # this gets the rows
    def print_board(self):
        for row in [self.board[ i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # displays which spot corresponds to which number
    @staticmethod
    def print_board_nums():
        # number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        number_board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # returns available moves index
    def available_moves(self):
        return [i for i , spot in enumerate(self.board) if spot == ' ']
    
    # returns T/F if there are still empty squares
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    # if valid move, then make the move (assign square to letter)
    # return true if valid, return false if invalid
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            # check for winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # get winner of the game, check if 3 in a row anywhere
    def winner(self, square, letter):
        # check row for winner
        row_idx = square // 3
        row = self.board[row_idx * 3 : (row_idx + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column for winner
        col_idx = square % 3
        column = [self.board[col_idx + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal for winner (0,4,8) or (2, 4, 6)
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag2]):
                return True
            
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter

    while game.empty_squares():
        # get move from the player/comp
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(f"{letter} has won!")
                    break

            letter = 'O' if letter == 'X' else 'X' # switch players
            # same as
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
        
        # time interval between each print_board
        time.sleep(0.8)

    if print_game and game.current_winner == None:
        print('It\'s a Tie.')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)