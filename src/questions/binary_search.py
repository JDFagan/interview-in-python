# Search infinite array via binary means
# import java.io. *;
# import java.util. *;
#
# / **
#   Given an infinite array of sorted ints, and a target int to find, return the index
#   of the target int
#   */
#
# class Solution {
#    public static void main(String[] args) {
#       Solution s = new Solution();
#       int[] x =  {1, 2, 3};
#       assert s.findTarget(x, 2) == 1;
#       assert s.findTarget(x, 5) == -1;
#       assert s.findTarget(x, 1) == 0;
#    }
#
#    public int findTarget(int[] array, int target) {
#       for (int i = 0; i < array.length; i *= 2) {
#          if (array[i] == target) {
#             return i;
#          } else if (array[i] > target) {
#             int low = i / 2;
#             int high = i;
#             return runBinarySearch(array, target, low, high);
#          }
#       }
#       return -1;
#    }
# }
import random

def infinite_list(x, y):
    n = x
    while True:
        n += y
        yield n


def find(array, target):
    for i in range(len(array), step=i*2)

list_max = 100
stream_list = []
for n in infinite_list(0, 1):
    stream_list.append(n)
    # print(n)
    if n == list_max:
        break
target = random.randrange(list_max)

print(f"Finished generating infinite list, stream_list = {stream_list}")
