import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        length: int = 0
        for val in collections.Counter(s).values():
            length += val // 2 * 2
            if length % 2 == 0 and val % 2 == 1:
                length += 1
        return length


print(Solution().longestPalindrome(s="abccccdd"))
