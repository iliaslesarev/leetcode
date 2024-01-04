from collections import Counter


def least_time(tasks, n):
    frequencies = Counter(tasks)
    frequencies = sorted(frequencies.values(), reverse=True)

    result = 0
    idle_time = (frequencies[0] - 1) * n

    for i in range(1, len(frequencies)):
        idle_time -= min(frequencies[0] - 1, frequencies[i])
        result += frequencies[i]

    if idle_time > 0:
        result += idle_time

    return result + frequencies[0]


print(least_time(["A", "C", "B", "A"], 0))
# print(least_time(["C", "A", "B", "A", "A", "B"], 3))
print(least_time(["A", "A", "B", "B"], 2))
