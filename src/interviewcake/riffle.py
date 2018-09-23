# O(n) time and O(1) space
def is_single_riffle(shuffled_deck: [], half1: [], half2: []):
    if len(shuffled_deck) != len(half1) + len(half2):
        raise IndexError("Invalid inputs - deck size does not equal sum of the size of the halves")

    h1 = h2 = 0
    for card in shuffled_deck:
        print("card = {}, h1 = {}, h2 = {}".format(card, h1, h2))
        if h1 < len(half1) and card == half1[h1]:
            h1 += 1
        elif h2 < len(half2) and card == half2[h2]:
            h2 += 1
        else:
            return False

    return True
