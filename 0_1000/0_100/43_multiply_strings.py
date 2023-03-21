class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num2)):
            remember = 0
            j = 0
            while j < len(num1):
                multiply_res = int(num1[j]) * int(num2[i]) + remember
                remember, r = divmod(multiply_res, 10)
                res[i + j] += r
                j += 1
            res[i + j] += remember

        for i in range(len(res) - 1):
            div, reminder = divmod(res[i], 10)
            res[i] = reminder
            res[i + 1] += div

        summary = 0
        for i in range(len(res)):
            summary += res[i] * 10 ** i
        return str(summary)


print(Solution().multiply("999", "999"))
print(Solution().multiply("123", "456"))
