def get_products_of_all_ints_except_at_index(integers):
    # Handle edge cases
    if len(integers) < 1:
        raise IndexError('Getting products requires at least 1 integer')
    if len(integers) == 1:
        return [None]

    # Initialize empty list of products
    products = [1] * len(integers)

    # Brute force solution requiring O(n^2) time and O(n) space
    for i in range(len(integers)):
        for j in range(len(integers)):
            if j != i:
                products[i] = products[i]*integers[j]

    return products
