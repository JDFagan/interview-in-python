# O(n + k) time and O(n + k) space where k is max value expected in array
def counting_sort(array, k):
    # init histogram with zeros
    counts = [0]*(k+1)

    # populate histogram of value frequencies
    for a in array:
        counts[a] += 1               # histogram of array's values

    result = []

    # for each i (the value), and item (the count) in counts
    for i, item in enumerate(counts):
        # for the count the value occurs
        for time in range(item):
            # add the value to the sorted list
            result.append(i)

    return result
