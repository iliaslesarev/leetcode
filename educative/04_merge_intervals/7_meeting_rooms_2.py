import heapq


def find_sets(intervals):
    intervals.sort(key=lambda x: x[0])
    rooms = [intervals[0][1]]
    heapq.heapify(rooms)

    for interval in intervals[1:]:
        if interval[0] < rooms[0]:
            heapq.heappush(rooms, interval[1])
        else:
            heapq.heapreplace(rooms, interval[1])

    return len(rooms)


print(find_sets([[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]))
print(find_sets([[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]))
