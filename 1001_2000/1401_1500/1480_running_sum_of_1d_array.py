from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        sum: int = 0
        for num in nums:
            sum += num
            result.append(sum)
        return result

    def runningSum2(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        return nums


nums = [1, 2, 3, 4]
print(Solution().runningSum2(nums))
