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
from pandas import *
import copy


class ConnectFour:
    def __init__(self, num_cols=7, num_rows=6):
        self.num_cols = num_cols
        col = [0] * num_rows
        self.new_board = [col] * num_cols
        print(DataFrame(self.new_board))

    def check_seq(self, squares):
        player1_seq = 0
        player2_seq = 0

        for square in squares:
            if square == 1:
                player1_seq += 1
                player2_seq = 0
            else:
                player1_seq = 0
                player2_seq += 1
            if player1_seq == 4:
                return 1
            elif player2_seq == 4:
                return 2

        return 0

    def play_game(self, game: []):
        board = copy.deepcopy(self.new_board)
        pieces_by_col = [0] * self.num_cols
        player = 1
        for col in game:
            c = col - 1
            board[c][pieces_by_col[c]] = player
            pieces_by_col[c] += 1
            player = 2 if player == 1 else 1

        print()
        print(DataFrame(board))
        print()
        print(DataFrame(board[::-1]))
        print()
        return None


cf = ConnectFour()
print(cf.play_game(game=[1, 2, 1, 3, 1, 4, 1]))
print(cf.play_game(game=[2, 1, 3, 1, 4, 1, 6, 1]))
print(cf.play_game(game=[2, 1, 3, 1, 4, 1, 5, 1]))
