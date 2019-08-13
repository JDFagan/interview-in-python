# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
#
# Input Format
# The first line contains . The second line contains an array   of  integers each separated by a space.
def runner_up(n, array):
    if n < 2:
        return ValueError('n is less than 2')
    high = None
    next_high = None
    for num in array:
        if high is None:
            high = num
            print(f"num: {num} (high: {high}, next_high: {next_high})")
            continue
        if num > high:
            next_high = high
            high = num
        else:
            if next_high is None:
                if num < high:
                    next_high = num
            else:
                if next_high < num < high:
                    next_high = num
        print(f"num: {num} (high: {high}, next_high: {next_high})")

    return next_high


print(runner_up(5, [2, 3, 6, 6, 5]))
print(runner_up(4, [57, 57, -57, 57]))
