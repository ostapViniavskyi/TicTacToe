# Module with class representing a board for playing TicTacToe game
from btree import Tree


class Board:
    FIRST_MARK = 'X'
    SECOND_MARK = 'O'
    WINNING_COMBINATIONS = [((0, i), (1, i), (2, i)) for i in range(3)] + \
                           [((i, 0), (i, 1), (i, 2)) for i in range(3)] + \
                           [((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))]

    def __init__(self):
        """Create empty board instance"""
        self.board = [[None for i in range(3)] for j in range(3)]
        self.last_move = None

    @classmethod
    def new_board(cls, board, move):
        """Creates new board instance that is copy of board and adds move
        to it
        move must be in the next format: (symbol, (coord1, coord2))"""
        result_board = cls()
        for i in range(3):
            for j in range(3):
                result_board.board[i][j] = board.board[i][j]
        result_board.board[move[1][0]][move[1][1]] = move[0]
        result_board.last_move = move
        return result_board

    def current_state(self, first_player=1):
        """Return -1 if state is winning for first player
                   0 if state is a draw
                   1 if state is a lose for first player
               None if game is not finished yet
               first_player: 1 - if human plays for X
                             0 - if computer plays for X"""
        # check for winning state for both sides
        for x in Board.WINNING_COMBINATIONS:
            if self.board[x[0][0]][x[0][1]] == self.board[x[1][0]][x[1][1]] \
                    == self.board[x[2][0]][x[2][1]]:
                if self.board[x[0][0]][x[0][1]] == Board.FIRST_MARK:
                    return -1 if first_player else 1
                if self.board[x[0][0]][x[0][1]] == Board.SECOND_MARK:
                    return 1 if first_player else -1
        # check for draw
        is_draw = True
        for row in self.board:
            for cell in row:
                if cell is None:
                    is_draw = False
        if is_draw:
            return 0
        # game not finished yet
        return None

    def __eq__(self, other):
        equal = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != other.board[i][j]:
                    equal = False
        return equal

    def __str__(self):
        """Return str(self)"""
        board = ''
        board += '   |   |\n'
        board += ' ' + (self.board[0][0] if self.board[0][0] else ' ') + \
                 ' | ' + (self.board[0][1] if self.board[0][1] else ' ') + \
                 ' | ' + (self.board[0][2] if self.board[0][2] else ' ')
        board += '\n   |   |\n-----------\n   |   |\n'
        board += ' ' + (self.board[1][0] if self.board[1][0] else ' ') + \
                 ' | ' + (self.board[1][1] if self.board[1][1] else ' ') + \
                 ' | ' + (self.board[1][2] if self.board[1][2] else ' ')
        board += '\n   |   |\n-----------\n   |   |\n'
        board += ' ' + (self.board[2][0] if self.board[2][0] else ' ') + \
                 ' | ' + (self.board[2][1] if self.board[2][1] else ' ') + \
                 ' | ' + (self.board[2][2] if self.board[2][2] else ' ')
        board += '\n   |   |\n'
        return board


if __name__ == '__main__':
    b = Board()
    print(b)
