from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []

        for j in range(n):
            i = step = 0
            while True:
                if i == m:
                    res.append(j)
                    break
                if j == -1 or j == n:
                    res.append(-1)
                    break

                cur_val = grid[i][j]
                if step == 0:
                    j += cur_val
                    step = cur_val
                elif step == cur_val:
                    step = 0
                    i += 1
                else:
                    res.append(-1)
                    break

        return res


print(Solution().findBall(
    grid=[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
print(Solution().findBall(grid=[[-1]]))
