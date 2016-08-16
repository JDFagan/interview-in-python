from functools import reduce # Valid in Python 2.6+, required in Python 3
# import operator

def get_products_of_all_ints_except_at_index(integers):
    # Handle edge cases
    if len(integers) < 1:
        raise IndexError('Getting products requires at least 1 integer')
    if len(integers) == 1:
        return [None]

    # Initialize  list of products
    products = [None] * len(integers)

    # Reduce solution requiring O(n) time and O(n) space
    for i in range(len(integers)):
        left = integers[:i]
        right = integers[i + 1:]
        products[i] = reduce(lambda x, y: x*y, left + right)

    return products
