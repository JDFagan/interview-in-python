"""
Task
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format
The first and only line contains the integer, .

Constraints
1 <= n <= 20

Output Format
Print  lines, one corresponding to each .

Sample Input
5

Sample Output
0
1
4
9
16
"""
if __name__ == '__main__':
    n = int(input("Enter an integer to see its squared range:  "))

    # for i in range(n):
    #     print(i ** 2)
    [print(i ** 2) for i in range(n)]
