# O(n + k) time (via counting sort) and O(k) space where k is the unique key set of movie lengths
# Worst space is O(n) if all movie lengths are unique, otherwise less than n
def are_two_movie_runtimes_within_flight_time(flight_length : int, movie_lengths : []):
    # function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes)
    # and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
    # When building your function:
    #   - Assume your users will watch exactly two movies
    #   - Don't make your users watch the same movie twice
    #   - Optimize for runtime over memory

    if len(movie_lengths) < 2:
        return False

    sorted_movie_lengths = sorted(movie_lengths)
    return sorted_movie_lengths[0] + sorted_movie_lengths[1] <= flight_length
