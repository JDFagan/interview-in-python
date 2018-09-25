"""
Lyric would like you to design a simple program to play a two person game of connect 4.  Connect 4 is a
two-player game in which the players take turns dropping discs — matched to each player — from the
top into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying
the next available space within the column. The objective of the game is to be the first to form a
horizontal, vertical, or diagonal line of four of one's own discs.

Your implementation should have a main interface that takes one parameter, an array of integers
representing the alternating plays for players one and two and that returns 1 if player one wins,
2 if player 2 wins, and 0 if no one wins (either a draw or an incomplete game).

For example, if the input was [1,2,1,3,1,4,1] then player 1 has a vertical connect four in the first
column, so the method should return 1 and input [2,1,3,1,4,1,6,1] should return 2.

An example interface in Ruby might look something like:
    winner = ConnectFour.new.play_game([1,2,1,3,1,4,1])
    puts "#{(winner == 1) ? '' : 'in'}correct winner: #{winner}"
"""
import numpy
import pandas


class ConnectFour:
    WINNING_SEQUENCE_COUNT = 4
    BOARD_ROWS = 6
    BOARD_COLS = 7

    def __init__(self, num_rows=BOARD_ROWS, num_cols=BOARD_COLS):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.player = None
        self.board: numpy.ndarray = None
        self.rows_played_by_col = None
        self.new_board()

    def play_game(self, game: []):
        winner = 0
        self.new_board()
        for col_played in game:
            col = col_played - 1
            winner = self.play_move(col)
            if winner:
                break
            self.player = 2 if self.player == 1 else 1

        # Print result of game
        self.print_board()
        if winner:
            print('  => Winner is player {}'.format(winner))
        else:
            print('  => There was no winner in this game')

        return winner

    def new_board(self):
        # self.board = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.board = numpy.zeros(shape=(self.num_rows, self.num_cols), dtype=numpy.int_)
        self.player = 1
        self.rows_played_by_col = [0] * self.num_cols

    def print_board(self):
        print(pandas.DataFrame(self.board))

    def play_move(self, col):
        """
        Modifies board based on current player's move
        :param col:
        :return:
        """
        # print()
        # self.print_board()
        # print()
        # print('col = {}, self.rows_played_by_col[col] = {}, self.player = {}'.format(col, self.rows_played_by_col[col], self.player))

        self.board[self.rows_played_by_col[col]][col] = self.player
        winner = self.winner(row=self.rows_played_by_col[col], col=col)
        self.rows_played_by_col[col] += 1
        return winner

    def winner(self, row, col):
        """
        Evaluates from current cell whether a winning move has been detected.  It's easy to
        determine if winner is on vertical column.  We'll take advantage of this by re-using
        vertical_winner method multiple times to see if winner is vertical, horizontal or diagonal:
        * vertical: pass in board as is
        * horizontal: flip board's rows and columns via zip method (equivalent of 90 degree board rotation)
        * diagonal: use numpy's diag to pull out the diagonals of the board

        :return: 0 if no winner, 1 or 2 if player 1 vs. player 2 is winner
        """
        winning_seq = (self.player,) * self.WINNING_SEQUENCE_COUNT

        # Check for vertical wins
        print('...checking for vertical win...')
        winner = self.vertical_winner(board=self.board, row=row, col=col, winning_seq=winning_seq)
        if winner:
            return winner

        # Check for horizontal wins
        print('...checking for horizontal win...')
        winner = self.horizontal_winner(board=self.board, row=row, col=col, winning_seq=winning_seq)
        if winner:
            return winner

        # Check for diagonal wins
        diags = [self.board[::-1, :].diagonal(i) for i in range(-self.board.shape[0] + 1, self.board.shape[1])]
        diags.extend(self.board.diagonal(i) for i in range(self.board.shape[1] - 1, -self.board.shape[0], -1))
        diag_board = [n.tolist() for n in diags]
        print('...checking for diagonal win...')
        winner = self.horizontal_winner(board=diag_board, row=row, col=col, winning_seq=winning_seq)

        return winner

    def vertical_winner(self, board, row, col, winning_seq):
        """
        Check for vertical win

        :param board:
        :param row:
        :param col:
        :param winning_seq: Winning pattern to search for
        :return:
        """
        winner = 0
        r = row + 1
        if r >= self.WINNING_SEQUENCE_COUNT:
            board_by_cols = [c for c in zip(*board)]
            col_ = board_by_cols[col]
            seq = col_[r - self.WINNING_SEQUENCE_COUNT:r]
            if seq == winning_seq:
                winner = self.player
        return winner

    def horizontal_winner(self, board, row, col, winning_seq):
        """
        Check for horizontal win

        :param board:
        :param row:
        :param col:
        :param winning_seq: Winning pattern to search for
        :return:
        """
        winner = 0
        r = row + 1
        start_window = max(r - self.WINNING_SEQUENCE_COUNT, 0)
        end_window = start_window + self.WINNING_SEQUENCE_COUNT
        windows = [(max(sw, 0), min(sw + self.WINNING_SEQUENCE_COUNT, self.BOARD_COLS)) for sw in range(start_window, end_window)]
        print(board)
        # print('row ({}), col ({}), windows = {}'.format(row, col, windows))

        for window in windows:
            row_ = board[row]
            seq = tuple(row_[window[0]:window[1]])
            print('Comparing seq ({}) to winning_seq ({})'.format(seq, winning_seq))
            if seq == winning_seq:
                winner = self.player
                break

        return winner

    def diagonal_winner(self, board):
        winner = 0

        # for diag in board:
        pass
    