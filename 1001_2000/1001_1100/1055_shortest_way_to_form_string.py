class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, res = 0, 1

        for l in target:
            i = source.find(l, i)

            if i == -1:
                res += 1
                i = source.find(l)
                if i == -1:
                    return -1
            i += 1
        return res


print(Solution().shortestWay(source="abc", target="abcbc"))
print(Solution().shortestWay(source="abc", target="acdbc"))
print(Solution().shortestWay(source="xyz", target="xzyxz"))
print(Solution().shortestWay(source="aaaaa", target="aaaaaaaaaaaaa"))
