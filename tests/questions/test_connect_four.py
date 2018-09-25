import numpy
import pytest

from questions.connect_four import ConnectFour


@pytest.fixture()
def board():
    return numpy.array([
        [1, 2, 2, 0, 0, 0, 3],
        [1, 0, 2, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        ])


def test_get_diagonals1(board):
    row = 0
    col = 2
    expected_diagonals = {
        'down_diagonal': [2, 0, 0, 0, 0],
        'up_diagonal': [1, 0, 2],
        }
    diagonals = ConnectFour.get_diagonals(board, row, col)
    assert expected_diagonals == diagonals


def test_get_diagonals2(board):
    row = 2
    col = 2
    expected_diagonals = {
        'down_diagonal': [1, 0, 0, 0, 0, 0],
        'up_diagonal': [0]*5,
        }
    diagonals = ConnectFour.get_diagonals(board, row, col)
    assert expected_diagonals == diagonals


def test_get_diagonals3(board):
    row = 2
    col = 1
    expected_diagonals = {
        'down_diagonal': [1, 0, 0, 0, 0],
        'up_diagonal': [1, 0, 2, 0],
        }
    diagonals = ConnectFour.get_diagonals(board, row, col)
    assert expected_diagonals == diagonals


def test_get_diagonals4(board):
    row = 0
    col = 6
    expected_diagonals = {
        'down_diagonal': [3],
        'up_diagonal': [0, 0, 0, 0, 0, 3],
        }
    diagonals = ConnectFour.get_diagonals(board, row, col)
    assert expected_diagonals == diagonals


def test_game_empty():
    game = []
    cf = ConnectFour()
    assert 0 == cf.play_game(game)


def test_game_no_winner():
    game = [1, 2, 1, 3, 1, 4]
    cf = ConnectFour()
    assert 0 == cf.play_game(game)


def test_game_vertical_win_player_1():
    game = [1, 2, 1, 3, 1, 4, 1]
    cf = ConnectFour()
    assert 1 == cf.play_game(game)


def test_game_vertical_win_player_2():
    game = [1, 2,
            1, 3,
            1, 1,
            2, 3,
            4, 3,
            5, 3,
            ]
    cf = ConnectFour()
    assert 2 == cf.play_game(game)


def test_game_horizontal_win_player_1():
    game = [3, 3,
            5, 5,
            4, 6,
            2
            ]
    cf = ConnectFour()
    assert 1 == cf.play_game(game)


def test_game_horizontal_win_player_2():
    game = [1, 2, 2, 3, 1, 4, 1, 5]
    cf = ConnectFour()
    assert 2 == cf.play_game(game)


def test_game_diagonal_down_win_player_1():
    game = [1, 2,
            2, 3,
            4, 3,
            3, 5,
            4, 4,
            4
            ]
    cf = ConnectFour()
    assert 1 == cf.play_game(game)


def test_game_diagonal_up_win_player_1():
    game = [1, 1,
            1, 2,
            1, 1,
            2, 3,
            3, 3,
            4, 5,
            2
            ]
    cf = ConnectFour()
    assert 1 == cf.play_game(game)
