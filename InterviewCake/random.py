import random


def rand5():
    return random.randint(1, 5)


def rand7():
    return random.randint(1, 7)


def rand5_biased():
    # A bad/biased solution which overweights values 2 and 3 due to remainder values > 5 and <= 7

    return rand7() % 5 + 1


# O(inf) time and O(1) space
def rand5_cake():
    # Constraint - can only make use of rand7 function.  How to make rand5_die return random (and uniform distribution)
    # of numbers?
    result = 7

    while result > 5:
        result = rand7()

    return result


# O(5) time and O(1) space
def rand5_die():
    # Constraint - can only make use of rand7 function.  How to make rand5_die return random (and uniform distribution)
    # of numbers?

    return (rand7() + rand7() + rand7() + rand7() + rand7()) % 5 + 1


def rand5_biased():
    # A bad/biased solution which overweights values 2 and 3 due to remainder values > 5 and <= 7

    return rand7() % 5 + 1


# O(inf) time and O(1) space
def rand7_biased():
    # Constraint - can only make use of rand5 function.  How to make rand7_die return random (and uniform distribution)
    # of numbers?
    result = 10
    while result > 7:
        result = rand5() + rand5()

    return result


# O(inf) time and O(1) space
def rand7_cake():
    while True:
        # do our die rolls
        roll1 = rand5()
        roll2 = rand5()

        outcome_number = (roll1-1) * 5 + (roll2-1) + 1

        # if we hit an extraneous
        # outcome we just re-roll
        if outcome_number > 21:
            continue

        # our outcome was fine. return it!
        return outcome_number % 7 + 1


# O(7) time and O(1) space
def rand7_die():
    # Constraint - can only make use of rand5 function.  How to make rand7_die return random (and uniform distribution)
    # of numbers?

    return (rand5() + rand5() + rand5() + rand5() + rand5() + rand5() + rand5()) % 7 + 1
