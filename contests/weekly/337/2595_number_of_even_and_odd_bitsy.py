from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        index = 0
        res = [0, 0]
        while n != 0:
            n, remainder = divmod(n, 2)
            if remainder != 0:
                if index % 2 == 0:
                    res[0] += 1
                else:
                    res[1] += 1
            index -= 1
        return res


print(Solution().evenOddBit(17))
print(Solution().evenOddBit(1))
print(Solution().evenOddBit(2))
print(Solution().evenOddBit(4))
