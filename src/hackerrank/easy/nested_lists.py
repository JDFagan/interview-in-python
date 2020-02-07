python_students = []
lowest = None
second_lowest = None
for _ in range(int(input())):
    name = input()
    score = float(input())
    python_students.append([name, score])
    if lowest is None:
        lowest = score
    else:
        if score < lowest:
            second_lowest = lowest
            lowest = score
        else:
            if second_lowest is None:
                if score > lowest:
                    second_lowest = score
            else:
                if lowest < score < second_lowest:
                    second_lowest = score

print(python_students)
# print(f"Lowest score: {lowest}, Second Lowest score: {second_lowest}")
# print(f"Names of python_students: {[s[0] for s in python_students]}")
second_lowest_scorers = [ps[0] for ps in python_students if ps[1] == second_lowest]
second_lowest_scorers.sort()
[print(sls) for sls in second_lowest_scorers]
# print(f"Second lowest scorers: {second_lowest_scorers}")
