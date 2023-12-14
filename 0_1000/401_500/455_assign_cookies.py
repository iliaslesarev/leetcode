from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                j += 1
            i += 1
        return j


print(Solution().findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(Solution().findContentChildren(g=[1, 2], s=[1, 2, 3]))
