from InterviewCake.inflight_entertainment import *


def test_no_elements():
    assert not are_two_movie_runtimes_within_flight_time(60, [])


def test_one_element():
    assert not are_two_movie_runtimes_within_flight_time(60, [45])


def test_movies1():
    movie_lengths = [120, 180, 90, 79, 88]
    assert not are_two_movie_runtimes_within_flight_time(70, movie_lengths)
    assert are_two_movie_runtimes_within_flight_time(200, movie_lengths)
