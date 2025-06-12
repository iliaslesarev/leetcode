import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        buy_price = sys.maxsize
        for price in prices:
            if price < buy_price:
                buy_price = price
            max_profit = max(max_profit, price - buy_price)
        return max_profit


print(Solution().maxProfit(prices=[7,1,5,3,6,4]))
print(Solution().maxProfit(prices=[3,3,5,0,0,3,1,4]))
