import random


def rand7():
    # The function that we are constrained to use

    return random.randint(1, 7)


def rand5_biased():
    # A bad/biased solution which overweights values 2 and 3 due to remainder values > 5 and <= 7

    return rand7() % 5 + 1


def rand5():
    # Constraint - can only make use of rand7 function.  How to make rand5 return random (and uniform distribution)
    # of numbers?

    return (rand7() + rand7() + rand7() + rand7() + rand7()) % 5 + 1
