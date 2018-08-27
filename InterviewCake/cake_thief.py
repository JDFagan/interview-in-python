import bisect
import math


# Tactic is to first order by normalized values by one unit of weight and fill duffel bag first by this ordering.
# Note: my solution is faster algorithm that gives us a good answer, even if it's not the optimal answer.
# Sometimes an efficient, good answer might be more practical than an inefficient, optimal answer.
# O(n) time and O(n) space
def max_duffel_bag_value(cake_tuples, capacity):
    cakes_by_value_per_weight = []
    for i in range(len(cake_tuples)):
        cake_tuple = cake_tuples[i]
        cake_weight = cake_tuple[0]
        cake_value = cake_tuple[1]
        cake_value_per_weight = cake_value/cake_weight if cake_weight > 0 else math.inf*cake_value
        bisect.insort(cakes_by_value_per_weight, (cake_value_per_weight, i))

    result = 0
    for i in reversed(range(len(cakes_by_value_per_weight))):
        cake_index = cakes_by_value_per_weight[i][1]
        cake_weight = cake_tuples[cake_index][0]
        cake_value = cake_tuples[cake_index][1]
        cakes = capacity//cake_weight if cake_weight > 0 else math.inf
        result += cakes*cake_value if cake_value > 0 else 0
        if result >= math.inf:
            break
        capacity -= cakes*cake_weight

    return result
