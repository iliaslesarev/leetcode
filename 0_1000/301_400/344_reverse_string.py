from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1


s = ["a", "b", "c", "d"]
s = []
s = ["a", "a"]
Solution().reverseString(s=s)
print(s)
