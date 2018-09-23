def test_no_elements():
    numbers = []
    assert find_duplicate_number_not_in_a_range(numbers) is None


def test_one_elements():
    numbers = [1]
    assert find_duplicate_number_not_in_a_range(numbers) is None


def test_dup0():
    numbers = [1, 2, 3]
    assert find_duplicate_number_not_in_a_range(numbers) is None


def test_dup1():
    numbers = [1, 2, 3, 3, 4]
    assert find_duplicate_number_not_in_a_range(numbers) == 3


def test_dup2():
    numbers = [1, 1, 2, 3]
    assert find_duplicate_number_not_in_a_range(numbers) == 1


def test_range_no_elements():
    numbers = []
    assert find_duplicate_number_in_range(numbers) == 0


def test_range_one_elements():
    numbers = [1]
    assert find_duplicate_number_in_range(numbers) == 0


def test_range_dup0():
    numbers = [1, 2, 3]
    assert find_duplicate_number_in_range(numbers) == 0


def test_range_dup1():
    numbers = [1, 2, 3, 3, 4]
    assert find_duplicate_number_in_range(numbers) == 3


def test_range_dup2():
    numbers = [1, 1, 2, 3]
    assert find_duplicate_number_in_range(numbers) == 1
