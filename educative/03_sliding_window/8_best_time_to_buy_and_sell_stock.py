def max_profit(prices):
    if len(prices) <= 1:
        return 0

    buy = profit = 0

    for sell in range(1, len(prices)):
        if prices[sell] < prices[buy]:
            buy = sell
        else:
            profit = max(prices[sell] - prices[buy], profit)

    return profit


print(max_profit([1, 5]))  # 4
print(max_profit([3, 2, 1, 2, 5]))  # 4
print(max_profit([1]))  # 0
print(max_profit([4, 3, 2]))  # 0
