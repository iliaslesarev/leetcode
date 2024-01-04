class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
            "(" + str(self.start) + ", " + str(self.end) + ")"


from heapq import heapify, heappop, heappush


def employee_free_time(schedule):
    output = []

    heap = [(employee[0].start, i, 0) for i, employee in enumerate(schedule)]
    heapify(heap)

    _, i, j = heap[0]
    previous = schedule[i][j].start

    while heap:
        _, i, j = heappop(heap)

        if previous < schedule[i][j].start:
            output.append(Interval(previous, schedule[i][j].start))

        previous = max(previous, schedule[i][j].end)

        if j + 1 < len(schedule[i]):
            heappush(heap, (schedule[i][j + 1].start, i, j + 1))

    return output


print(employee_free_time([
    [Interval(3, 4), Interval(5, 6), Interval(8, 9)],
    [Interval(1, 3), Interval(5, 6), Interval(8, 9)],
    [Interval(6, 8)]]))
