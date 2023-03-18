class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        amount, remainder = divmod(money, 8)
        if amount > children or amount == children and remainder != 0:
            return children - 1
        elif amount == children and remainder == 0:
            return children
        else:
            money -= children
            res, remainder = divmod(money, 7)
            if children - res > 1 or remainder != 3:
                return res
            else:
                return res - 1


print(Solution().distMoney(money=20, children=3))
print(Solution().distMoney(money=16, children=2))
print(Solution().distMoney(money=7, children=2))
print(Solution().distMoney(money=7, children=7))
print(Solution().distMoney(money=5, children=2))
print(Solution().distMoney(money=13, children=3))
print(Solution().distMoney(money=17, children=2))
