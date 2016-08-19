# O(1) time and O(n) space
def get_rectangular_intersection(r1: dict, r2: dict):
    if {'left_x', 'bottom_y', 'width', 'height'} != r1.keys() or r1.keys() != r2.keys():
        raise TypeError("Rectangle dictionary input(s) not to specification")

    r1x1 = r1['left_x']
    r1x2 = r1x1 + r1['width']
    r1y1 = r1['bottom_y']
    r1y2 = r1y1 + r1['height']

    r2x1 = r2['left_x']
    r2x2 = r2x1 + r2['width']
    r2y1 = r2['bottom_y']
    r2y2 = r2y1 + r2['height']

    # Rule out no intersection first
    if not(r1x1 <= r2x1 <= r1x2) and not(r2x1 <= r1x1 <= r2x2):
        if not(r1y1 <= r2y1 <= r1y2) and not(r2y1 <= r1y1 <= r2y2):
            return None

    result = {}

    if r1x1 <= r2x1:
        result['left_x'] = r2x1

        if r1x2 <= r2x2:
            result['width'] = r1x2 - r2x1
        else:
            result['width'] = r2['width']       # embedded case
    else:
        result['left_x'] = r1x1

        if r1x2 <= r2x2:
            result['width'] = r1['width']       # embedded case
        else:
            result['width'] = r2x2 - r1x1

    if r1y1 <= r2y1:
        result['bottom_y'] = r2y1

        if r1y2 <= r2y2:
            result['height'] = r1y2 - r2y1
        else:
            result['height'] = r2['height']     # embedded case
    else:
        result['bottom_y'] = r1y1

        if r1y2 <= r2y2:
            result['height'] = r1['height']       # embedded case
        else:
            result['height'] = r2y2 - r1y1

    return result
