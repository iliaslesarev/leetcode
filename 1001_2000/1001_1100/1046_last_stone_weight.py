import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            max_val = heapq.heappop(stones)
            prev_max_val = heapq.heappop(stones)
            heapq.heappush(stones, max_val - prev_max_val)

        return -stones[0] if stones else 0


print(Solution().lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
