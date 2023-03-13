from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if len(words) <= j or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False
        return True


print(Solution().validWordSquare(words=["abcd", "bnrt", "crmy", "dtye"]))
print(Solution().validWordSquare(words=["abcd", "bnrt", "crm", "dt"]))
print(Solution().validWordSquare(words=["ball", "area", "read", "lady"]))
print(Solution().validWordSquare(words=["ball", "asee", "let", "lep"]))
