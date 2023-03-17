from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            middle = (i + j) // 2

            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                j = middle - 1
            else:
                i = middle + 1
        return -1


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2))
