from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        res = 0
        for i, num in enumerate(nums):
            if nums[i] + diff in s and nums[i] + 2 * diff in s:
                res += 1

        return res


print(Solution().arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3))
