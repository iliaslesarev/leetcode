class Solution:
    def climbStairs(self, n: int) -> int:
        w1, w2 = 1, 1
        for i in range(2, n + 1):
            tmp = w1 + w2
            w1 = w2
            w2 = tmp

        return w2
