class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        n, m = len(word1), len(word2)
        result = []
        while i < n or j < m:
            if i < n:
                result.append(word1[i])
            if j < m:
                result.append(word2[j])
            i += 1
            j += 1

        return "".join(result)
