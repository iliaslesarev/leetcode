class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[-1][-1]

print(Solution().uniquePaths(100,100))