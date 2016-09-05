from InterviewCake.temperature import *


def test_no_elements():
    tt = TempTracker()
    assert tt.get_max() is None
    assert tt.get_min() is None
    assert tt.get_mean() is None
    assert tt.get_mode() is None


def test_temps1():
    tt = TempTracker()
    temps = [67]
    tt.insert(temps[0])
    assert tt.get_max() == 67
    assert tt.get_min() == 67
    assert tt.get_mean() == 67
    assert tt.get_mode() == 67


def test_temps2():
    tt = TempTracker()
    temps = [67, 69]
    tt.insert(temps[0])
    tt.insert(temps[1])
    assert tt.get_max() == 69
    assert tt.get_min() == 67
    assert tt.get_mean() == 68
    assert tt.get_mode() == 67


def test_temps3():
    tt = TempTracker()
    temps = [67, 69, 97]
    tt.insert(temps[0])
    tt.insert(temps[1])
    tt.insert(temps[2])
    assert tt.get_max() == 97
    assert tt.get_min() == 67
    assert tt.get_mean() == (67 + 69 + 97)/3
    assert tt.get_mode() == 67


def test_temps4():
    tt = TempTracker()
    temps = [67, 69, 97, 97]
    tt.insert(temps[0])
    tt.insert(temps[1])
    tt.insert(temps[2])
    tt.insert(temps[3])
    assert tt.get_max() == 97
    assert tt.get_min() == 67
    assert tt.get_mean() == (67 + 69 + 97 + 97)/4
    assert tt.get_mode() == 97
