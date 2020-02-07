def get_h_index(citations: [int]) -> int:
    """
    The h-index is a metric that measures both the productivity and citation impact of a researcher.
    Specifically, a researcher's h-index is the largest number h such that the researcher has published
    h papers that have each been cited at least h times.

    :param citations: List of papers' citations.  Example: [1, 4, 1, 4, 2, 1, 3, 5, 6]
    :return: An integer representing the h-index value.
    """
    # O(n + k) or O(n log n)
    h_index = 0
    citations.sort()
    # [1, 1, 1, 2, 3, 4, 4, 5, 6]
    # 1: 1 + 8 >= 1 => 1
    # 1: 1 + 7 >= 1 => 1
    # 1: 1 + 6 >= 1 => 1
    # 2: 1 + 5 >= 2 => 2
    # 3: 1 + 4 >= 3 => 3
    # 4: 1 + 3 >= 4 => 4

    # O(n)
    for i, citation in enumerate(citations):
        if len(citations[i:]) >= citation:
            h_index = citation
        if len(citations[i:]) < citation:
            break

    # Total O = O(n + k) + O(n) = O(2n + k) = O(n + k) or O(n log n) depending on sort algorithm used
    return h_index
