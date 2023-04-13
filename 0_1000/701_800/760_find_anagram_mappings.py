from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {num: i for i, num in enumerate(nums2)}
        for i in range(len(nums1)):
            nums1[i] = a[nums1[i]]
        return nums1
