from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        max_satisfaction = suffix_sum = 0
        for i in range(len(satisfaction) -1, -1, -1):
            if suffix_sum + satisfaction[i] <= 0:
                break
            suffix_sum += satisfaction[i]
            max_satisfaction += suffix_sum
        return max_satisfaction

print(Solution().maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]))
