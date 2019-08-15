from hackerrank.medium.triplets import get_subsequences, is_geometric


def test_subsequences():
    print(get_subsequences([1, 2, 2, 4], seq_len=3))


def test_is_geometric():
    assert not is_geometric([1, 2, 2], 2)
    assert is_geometric([1, 2, 4], 2)
