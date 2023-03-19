from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        cur = (0, 0)
        n = len(grid)
        steps = [(1, 2), (2, 1),
                 (2, -1), (-1, 2),
                 (-2, 1), (1, -2),
                 (-2, -1), (-1, -2)]
        for i in range(n ** 2 - 1):
            founded = False
            for step in steps:
                possible_step = (cur[0] + step[0], cur[1] + step[1])
                if (0 <= possible_step[0] < n and
                        0 <= possible_step[1] < n and
                        grid[possible_step[0]][possible_step[1]] == i + 1):
                    cur = possible_step
                    founded = True
            if not founded:
                return False
        return True


print(Solution().checkValidGrid(
    grid=[[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]))
print(Solution().checkValidGrid(grid=[[0, 3, 6], [5, 8, 1], [2, 7, 4]]))
print(Solution().checkValidGrid(grid=[[0]]))
