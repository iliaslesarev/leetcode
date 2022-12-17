from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r_sum: int = sum(nums)
        l_sum: int = 0
        for i in range(len(nums)):
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1


nums = [-1, -1, 0, 1, 1, 0]
print(Solution().pivotIndex(nums))
