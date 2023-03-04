from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c0, c1 = cost[0], cost[1]

        for i in range(2, len(cost)):
            tmp = min(c0, c1) + cost[i]
            c0 = c1
            c1 = tmp

        return min(c0, c1)


print(Solution().minCostClimbingStairs(cost=[10,15,20]))
