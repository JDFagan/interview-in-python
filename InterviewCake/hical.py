# Takes a list of meeting time ranges and returns a list of condensed ranges.
# A meeting is stored as tuples of integers (start_time, end_time).
# Example: meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
def condense_meeting_times(meetings):
    if len(meetings) == 0 or len(meetings) == 1:
        return meetings

    meetings.sort()

    left = meetings[0]
    right = meetings[1]
    # rest = meetings[2:]
    rest = condense_meeting_times(meetings[2:])

    if (left <= right and right[0] <= left[1]) or (right <= left and left[0] <= right[1]):
        return condense_meeting_times([(min(left[0], right[0]), max(left[1], right[1]))] + rest)

    if left <= right:
        return [left] + condense_meeting_times([right] + rest)
    else:
        return [right] + condense_meeting_times([left] + rest)
