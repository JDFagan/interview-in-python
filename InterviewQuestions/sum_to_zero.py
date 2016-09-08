# Question by Hired

# Write function that returns any three numbers that sum to zero.  If none meet that criteria, return None.
# My first cut is brute force solution taking O(n^3) time and O(1) space
def get_three_that_sum_to_zero(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    return [nums[i], nums[j], nums[k]]

    return None
