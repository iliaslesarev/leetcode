import math
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def step(x, y):
            res.append(matrix[x][y])
            matrix[x][y] = -math.inf

        i, j, direction, res = 0, -1, 1, []
        while len(res) < len(matrix[0]) * len(matrix):
            while 0 <= j + direction < len(matrix[0]) and matrix[i][j + direction] > -math.inf:
                j += direction
                step(i, j)
            while 0 <= i + direction < len(matrix) and matrix[i + direction][j] > -math.inf:
                i += direction
                step(i, j)
            direction *= -1

        return res


print(Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(Solution().spiralOrder(matrix=[[1, 2], [3, 4]]))
