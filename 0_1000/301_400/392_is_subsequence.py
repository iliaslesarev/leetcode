class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        i = 0
        for l in t:
            if l == s[i]:
                i += 1
            if i == len(s):
                return True
        return False


print(Solution().isSubsequence(s="a", t="b"))
