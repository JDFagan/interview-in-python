def get_h_index(research_papers: dict) -> int:
    """
    The h-index is a metric that measures both the productivity and citation impact of a researcher.
    Specifically, a researcher's h-index is the largest number h such that the researcher has published
    h papers that have each been cited at least h times.

    :param research_papers: Dictionary of papers with keys being unique paper name and value being
    the number of citations that paper has had.  Example:
    {
        'A': 1,
        'B': 4,
        'C': 1,
        'D': 4,
        'E': 2,
        'F': 1,
        'G': 3,
        'H': 5,
        'I': 6,
    }
    :return: An integer representing the h-index value, which in above example would be 4.
    """
    # O(n)
    h_index = 0
    citation_papers = {}
    for paper, citations in research_papers.items():
        if citations in citation_papers:
            citation_papers[citations].append(paper)
        else:
            citation_papers[citations] = [paper]
    # print()
    # print(f"citation_papers = {citation_papers}")
    # print()

    # O(n + k) or O(n log n)
    sorted_citations = list(citation_papers.keys())
    sorted_citations.sort(reverse=True)
    # print(f"sorted_citations = {sorted_citations}")
    # print()

    # O(k)
    big_citations = 0
    for citations in sorted_citations:
        # print(f"len({citation_papers[citations]} + {big_citations} >= {citations}: "
        #       f"{len(citation_papers[citations])} + {big_citations} >= {citations}: "
        #       f"{len(citation_papers[citations]) + big_citations >= citations}")
        if len(citation_papers[citations]) + big_citations >= citations > h_index:
            h_index = citations
        big_citations += 1

    # Total O = O(2n + 2k) = O(n + k) or O(n log n) depending on the efficient sorting algorithm used
    return h_index
