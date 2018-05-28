# Module with class Game that controls the whole game flow
from board import Board
from btree import Tree
import os
import random


class Game:

    def __init__(self):
        """Create new Game instance"""
        self.board = Board()
        self.tree = None
        self.first_player = None

    def build_decision_tree(self):
        """Build decision tree for TicTacToe game"""
        self.tree = Tree()

        def recurse(board, node=None, player=self.first_player):
            """Recursively build tree of all possible
            moves in TicTacToe game
            player: 1 if human makes a move, 0 - if computer"""
            if node is None:
                curr_node = self.tree.add_root(board)
            else:
                curr_node = self.tree.add_child(node, board)

            # if current state is not final yet:
            curr_state = \
                curr_node.item.current_state(first_player=self.first_player)
            if curr_state is None:
                for i in range(3):
                    for j in range(3):
                        if curr_node.item.board[i][j] is None:
                            move = (Board.FIRST_MARK
                                    if player ^ self.first_player ^ 1 else
                                    Board.SECOND_MARK, (i, j))
                            next_board = Board.new_board(curr_node.item, move)
                            recurse(next_board, curr_node, player ^ 1)
                if player:
                    # consider that human makes the best move
                    curr_node.score = min(c.score for c in curr_node.children)
                else:
                    # try to make teh best move
                    curr_node.score = max(c.score for c in curr_node.children)

            else:
                curr_node.score = curr_state

        recurse(self.board)

    def generate_next_move(self):
        """Generate next move for bot"""
        self.tree._root = max(self.tree._root.children, key=lambda x: x.score)
        self.board = self.tree._root.item

    def read_player_move(self):
        """Read player move until it's in correct format"""
        while True:
            try:
                coord1 = int(input('Type first coordinate (0-2): '))
                coord2 = int(input('Type second coordinate (0-2): '))
                assert 0 <= coord1 <= 2 and 0 <= coord2 <= 2 and\
                    self.board.board[coord1][coord2] is None
                break
            except (ValueError, AssertionError):
                print('Try again')
                continue
        return coord1, coord2

    def make_player_move(self):
        """Make action after player entered his move"""
        move = (Board.FIRST_MARK if self.first_player else Board.SECOND_MARK,
                self.read_player_move())
        for child in self.tree._root.children:
            if child.item.last_move == move:
                self.tree._root = child
                break
        self.board = self.tree._root.item

    def check_for_end(self):
        """Check if game is ended"""
        state = self.board.current_state()
        if state is None:
            return False
        if state == -1:
            if self.first_player == 0:
                message = 'Lose. Better luck next time!'
            else:
                message = 'Victory!!!'
        elif state == 0:
            message = 'Draw.'
        else:
            if self.first_player == 1:
                message = 'Lose. Better luck next time!'
            else:
                message = 'Victory!!!'
        print(self.board)
        print(message)
        return True

    def play(self):
        """Control the main flow of the game"""
        # determine who is the first
        self.first_player = random.randint(0, 1)
        print('{} starts the game.'.format('Human' if self.first_player
                                           else 'Computer'))
        print('Preparing the game. Please wait...')
        self.build_decision_tree()
        # make computer first move
        if not self.first_player:
            self.generate_next_move()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.board)
            # move of player
            self.make_player_move()
            if self.check_for_end():
                break
            # move of computer
            self.generate_next_move()
            if self.check_for_end():
                break


if __name__ == '__main__':
    game = Game()
    game.play()


