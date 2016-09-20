# O(n) time and O(1) space
def find_repeating_num_in_range(nums_range: []):
    # We have a list of integers, where: The integers are in the range 1..n AND The list has a length of n+1
    # It follows that our list has at least one integer which appears at least twice. But it may have several duplicates,
    # and each duplicate may appear more than twice.
    # Write a function which finds any integer that appears more than once in our list.

    prev_num = 0
    for n in nums_range:
        if n == prev_num:
            return n
        prev_num = n

    return None
