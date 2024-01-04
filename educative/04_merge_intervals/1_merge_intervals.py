def merge_intervals(intervals):
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(intervals[i][1], result[-1][1])
        else:
            result.append(intervals[i])
    return result


print(merge_intervals([[1, 5], [2, 6], [3, 5], [9, 10]]))
print(merge_intervals([[1, 5]]))
print(merge_intervals([[1, 2], [3, 5], [4, 6]]))
