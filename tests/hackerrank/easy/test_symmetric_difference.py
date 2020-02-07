from hackerrank.easy import symmetric_difference


def test_1():
    input_values = ['9'
                    , '1 2 3 4 5 6 7 8 9'
                    , '9'
                    , '10 1 2 3 11 21 55 6 8']
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    symmetric_difference.input = mock_input
    symmetric_difference.print = lambda s: output.append(s)

    symmetric_difference.main()

    assert ['8'] == output
