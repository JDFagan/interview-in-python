# O(n) time and O(n) space
def find_duplicate_number_not_in_a_range(numbers: []):
    unique_numbers = set()
    for n in numbers:
        if n in unique_numbers:
            return n
        unique_numbers.add(n)

    return None


# O(n) time and O(1) space
def find_duplicate_number_in_range(number_range: []):
    if len(number_range) == 0:
        return 0

    sum_of_list = 0
    for n in number_range:
        sum_of_list += n

    n = number_range[len(number_range) - 1]
    triangular_series_sum = (n**2 + n)/2
    print("sum_of_list = {}, n = {}, triangular_series_sum = {}, dup_num = {}"
          .format(sum_of_list, n, triangular_series_sum, triangular_series_sum - sum_of_list))

    # Difference between triangular series and sum of list will be the duplicate number
    return sum_of_list - triangular_series_sum
