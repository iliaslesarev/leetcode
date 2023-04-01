from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        min_1 = min_2 = 10
        set_nums2 = set(nums2)
        res = 10
        for n in nums1:
            if n in set_nums2:
                res = min(res, n)
            else:
                min_1 = min(min_1, n)

        if res < 10:
            return res
        for n in nums2:
            min_2 = min(min_2, n)

        if min_1 < min_2:
            return min_1 * 10 + min_2
        else:
            return min_2 * 10 + min_1


print(Solution().minNumber(nums1=[3, 5, 2, 6], nums2=[1, 7]))
