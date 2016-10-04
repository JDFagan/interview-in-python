# Question by Meraki
# O(n) time and O(n) space where n is number of digits in the input
def do_digits_sum_to_target(num, target):
    digits = list(str(num))
    total = 0

    for d in digits:
        total += int(d)

    return total == target
