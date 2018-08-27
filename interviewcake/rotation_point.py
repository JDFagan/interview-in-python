# Modified version of binary search to find rotation point
# O(log(n)) time and O(1) space
def find_rotation_point(words):
    # return index of rotation point of alphabetically sorted list

    # we think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we /don't/ mean "the last index")
    floor_index = -1
    ceiling_index = len(words)

    # if there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present
    while floor_index + 1 < ceiling_index:
        # find the index ~halfway between the floor and ceiling
        # we use integer division, so we'll never get a "half index"
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        if words[guess_index] < words[guess_index - 1]:
            return guess_index

        if words[guess_index] < words[floor_index]:
            # target is to the left so move ceiling to the left
            ceiling_index = guess_index
        else:
            # target is to the right so move floor to the right
            floor_index = guess_index

    return -1
