# O(n) time and O(n) space
# Same problem Salesforce asked me as well and this was same code I wrote for it
def merge_lists(list1: [], list2: []):
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
