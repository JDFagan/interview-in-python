from typing import List


def adds_up_to_this_int(ints: List[int], target) -> bool:
    total = None
    for i in ints:
        if target is None:
            total = i
            continue
        total += i

    return target is total if total is None else target == total
