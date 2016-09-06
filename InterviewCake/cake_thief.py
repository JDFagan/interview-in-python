import bisect

# Tactic is to first order by normalized values by one unit of weight and fill duffel bag first by this ordering.
# O(n) time and O(n) space
def max_duffel_bag_value(cake_tuples, capacity):
    cakes_by_value_per_weight = []
    for i in range(len(cake_tuples)):
        cake_tuple = cake_tuples[i]
        bisect.insort(cakes_by_value_per_weight, (cake_tuple[1]/cake_tuple[0], i))

    result = 0
    for i in reversed(range(len(cakes_by_value_per_weight))):
        cake_index = cakes_by_value_per_weight[i][1]
        cake_weight = cake_tuples[cake_index][0]
        cake_value = cake_tuples[cake_index][1]
        cakes = capacity//cake_weight
        result += cakes*cake_value
        capacity -= cakes*cake_weight

    return result
