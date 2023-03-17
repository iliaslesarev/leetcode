from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                j = middle - 1
            else:
                i = middle + 1
        return i


print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
