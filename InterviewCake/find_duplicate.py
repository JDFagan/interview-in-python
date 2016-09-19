# O(n) time and O(n) space
def find_duplicate_number(numbers: []):
    unique_numbers = set()
    for n in numbers:
        if n in unique_numbers:
            return n
        unique_numbers.add(n)

    return None
