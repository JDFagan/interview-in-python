from functools import reduce


# Sort in O(n log(n)) time and O(n) space
def sort_high_to_low(integers):
    result = None
    for i in range(len(integers)):
        if result is None:
            result = [integers[i]]
            continue
        for j in range(len(result)):
            if integers[i] <= result[len(result)-1]:
                result += integers[i:i+1]
                break
            if integers[i] > result[j]:
                result = result[0:j] + integers[i:i+1] + result[j:]
                break

    return result


# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.
def get_highest_product(integers):
    if len(integers) < 3:
        raise IndexError("Input integers needs to be at least three integers")

    highest = max(integers[:2])
    lowest = min(integers[:2])
    highest_product_of_2 = lowest_product_of_2 = reduce(lambda x, y: x * y, integers[:2])
    highest_product_of_3 = reduce(lambda x, y: x * y, integers[:3])

    for current in integers[2:]:
        highest_product_of_3 = max(highest_product_of_3
                                   , current*highest_product_of_2
                                   , current*lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2
                                   , current*highest
                                   , current*lowest)
        lowest_product_of_2 = min(lowest_product_of_2
                                  , current*highest
                                  , current*lowest)

        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_3
