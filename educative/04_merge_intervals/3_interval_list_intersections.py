def intervals_intersection(interval_list_a, interval_list_b):
    output = []
    i = j = 0

    while i < len(interval_list_a) and j < len(interval_list_b):
        if (interval_list_b[j][0] <= interval_list_a[i][0] <= interval_list_b[j][1] or
                interval_list_a[i][0] <= interval_list_b[j][0] <= interval_list_a[i][1]):
            output.append([
                max(interval_list_a[i][0], interval_list_b[j][0]),
                min(interval_list_a[i][1], interval_list_b[j][1])])

        if interval_list_a[i][1] < interval_list_b[j][1]:
            i += 1
        else:
            j += 1

    return output


print(intervals_intersection([[1, 4], [7, 9]], [[3, 5], [6, 7], [8, 9]]))
print(intervals_intersection([], [[3, 5], [6, 7], [8, 9]]))
