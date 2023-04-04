class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        ss = set()
        for l in s:
            if l not in ss:
                ss.add(l)
            else:
                ss = set(l)
                res += 1
        return res


print(Solution().partitionString(s=""))
