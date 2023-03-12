from collections import Counter, defaultdict

from typing import Dict, List


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c: List[int] = [0] * 10
        bulls, cows = 0, 0
        for i, s in enumerate(secret):
            g = guess[i]

            if s == g:
                bulls += 1
            else:
                if c[int(s)] < 0:
                    cows += 1
                if c[int(g)] > 0:
                    cows += 1
                c[int(s)] += 1
                c[int(g)] -= 1

        return f"{bulls}A{cows}B"


print(Solution().getHint(secret="1807", guess="7810"))
print(Solution().getHint(secret="1123", guess="0111"))
print(Solution().getHint(secret="1122", guess="1222"))
print(Solution().getHint(secret="11", guess="10"))
