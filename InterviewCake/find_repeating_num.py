# O(log(n)) time and O(1) space
def find_repeating_num_in_range(nums_range: []):
    # We have a list of integers, where: The integers are in the range 1..n AND The list has a length of n+1
    # It follows that our list has at least one integer which appears at least twice.
    # But it may have several duplicates, and each duplicate may appear more than twice.
    # Write a function which finds any integer that appears more than once in our list.

    floor_index = -1
    ceiling_index = len(nums_range)
    has_duplicate = False

    # if there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present
    while floor_index + 1 < ceiling_index:
        # find the index ~halfway between the floor and ceiling
        # we use integer division, so we'll never get a "half index"
        distance = ceiling_index - floor_index
        half_distance = distance//2
        n_index = floor_index + half_distance
        n_value = nums_range[n_index]

        print("n_index = {}, n_value = {}".format(n_index, n_value))

        if n_value == n_index + 1:
            # duplicate is to the right so move floor to the right
            floor_index = n_index
        else:
            # a duplicate must exist
            has_duplicate = True
            ceiling_index = n_index

    if has_duplicate:
        return n_value

    # Couldn't find the repeating num
    return None
