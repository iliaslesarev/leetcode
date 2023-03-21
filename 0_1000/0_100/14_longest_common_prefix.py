from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            for line in strs:
                if i == len(line) or line[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


print(Solution().longestCommonPrefix(strs=["ab", "a"]))
