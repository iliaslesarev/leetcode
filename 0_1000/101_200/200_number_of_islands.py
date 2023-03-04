from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(x, y):
            if 0 <= x < height and 0 <= y < width and grid[x][y] == "1":
                grid[x][y] = "2"
                helper(x - 1, y)
                helper(x + 1, y)
                helper(x, y - 1)
                helper(x, y + 1)

        islands_amount, height, width = 0, len(grid), len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    helper(i, j)
                    islands_amount += 1
        return islands_amount
