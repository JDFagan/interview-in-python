def merge_lists(list1: [], list2: []):
    """
    O(n) time and O(n) space

    :param list1:
    :param list2:
    :return:
    """
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    if i < len(list1):
        result += list1[i:]
    elif j < len(list2):
        result += list2[j:]

    return result


# Insert: O(log(n)) time and O(n) space
# Inorder: O(n) time
#
# Bonus: What if we wanted to merge several sorted lists? Write a function that takes as an input a
# list of sorted lists and outputs a single sorted list with all the items from each list.
# Salesforce actually asked this bonus question too and perhaps I didn't answer this adequately enough as
# I said solution should still be O(n) time and O(n) space despite if one uses a binary search tree data
# structure for storing the intermediate sorting structure before generating the result.


# from sortedcontainers import SortedList


# def merge_many(list_of_sorted_lists: []):
#     result = []
#     sorted = SortedList()
#     for l in list_of_sorted_lists:
#         sorted.update(l)
#
#     for i in sorted:
#         result.append(i)
#
#     return result

def merge_many(list_of_sorted_lists: []):
    """
    Time: O(n + n * log n) = O(n * log n)
    Space: O(n)

    :param list_of_sorted_lists: list of sorted lists
    :return: sorted merged list of input
    """
    merged_sorted_lists = []
    for l in list_of_sorted_lists:
        merged_sorted_lists.extend(l)
    merged_sorted_lists.sort()
    return merged_sorted_lists
