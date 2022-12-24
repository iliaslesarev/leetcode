import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price: int = sys.maxsize
        max_sum: int = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_sum:
                max_sum = price - min_price

        return max_sum


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
