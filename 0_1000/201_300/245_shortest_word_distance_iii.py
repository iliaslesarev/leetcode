from typing import List


class Solution:

    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dist = len(wordsDict)
        first = second = -min_dist

        for i, word in enumerate(wordsDict):
            if word in [word1, word2]:
                if word1 == word2:
                    if first < second:
                        first = i
                    else:
                        second = i
                else:
                    if word == word1:
                        first = i
                    else:
                        second = i
                min_dist = min(min_dist, abs(second - first))

        return min_dist


print(Solution().shortestWordDistance(wordsDict=["practice", "makes", "perfect", "coding", "makes"],
                                      word1="makes",
                                      word2="makes"))
# print(Solution().shortestWordDistance(wordsDict=["a", "b"], word1="a", word2="b"))
