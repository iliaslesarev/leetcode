from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c: Dict[int, int] = {}
        for i, n in enumerate(nums):
            c[n] = i

        for i, n in enumerate(nums):
            if c.get(target - n) is not None and c.get(target - n) != i:
                return [i, c[target - n]]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))
print(Solution().twoSum(nums=[-3, 4, 3, 90], target=0))
