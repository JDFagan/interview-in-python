# O(n + k) time and O(k) space where k is max value expected in array
def counting_sort(array, k):
    # in-place counting sort

    count = [0] * k                 # init with zeros

    # calculate the histogram of key frequencies
    for a in array:
        count[a] += 1               # histogram of array's values

    i = 0
    for a in range(k):              # emit
        for _ in range(count[a]):   # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1

    return array
