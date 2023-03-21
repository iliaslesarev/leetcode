from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        amount, res = 0, 0
        for n in nums:
            if n == 0:
                amount += 1
            else:
                res += (1 + amount) / 2 * amount
                amount = 0
        if amount != 0:
            res += (1 + amount) / 2 * amount
        return int(res)


print(Solution().zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0]))
print(Solution().zeroFilledSubarray(nums=[1, 3, 0, 0, 2, 0, 0, 4]))
print(Solution().zeroFilledSubarray(nums=[]))
