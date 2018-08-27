import random

# O(n) time and O(1) space

# Fisher-Yates shuffling in place psuedocode:
# -- To shuffle an array a of n elements (indices 0..n-1):
# for i from n−1 downto 1 do
#      j ← random integer such that 0 ≤ j ≤ i
#      exchange a[j] and a[i]
def shuffle_inplace(items: []):
    for i in range(len(items) - 1, 1, -1):
        j = random.randint(0, i)
        print("random index = {}".format(j))
        items[i], items[j] = items[j], items[i]

    print("items = {}".format(items))

    return items
