def insert_interval(existing_intervals, new_interval):
    output = []

    i = 0
    while i < len(existing_intervals) and existing_intervals[i][0] < new_interval[0]:
        output.append(existing_intervals[i])
        i += 1

    if len(output) == 0 or output[-1][1] < new_interval[0]:
        output.append(new_interval)
    else:
        output[-1][1] = max(output[-1][1], new_interval[1])

    for j in range(i, len(existing_intervals)):
        if existing_intervals[j][0] <= output[-1][1]:
            output[-1][1] = max(output[-1][1], existing_intervals[j][1])
        else:
            output.append(existing_intervals[j])

    return output


print(insert_interval([[1, 3], [6, 8], [9, 11], [13, 16]], [4, 5]))
print(insert_interval([[1, 3], [6, 8], [9, 11], [13, 16]], [4, 10]))
print(insert_interval([[1, 3], [6, 8], [9, 11], [13, 16]], [17, 20]))
