from questions.connect_four import ConnectFour


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


def test_game_diagonal_win_player_1():
    game = [1, 2,
            2, 3,
            4, 3,
            3, 5,
            4, 4,
            4
            ]
    cf = ConnectFour()
    assert 1 == cf.play_game(game)
