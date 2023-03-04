class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f1, f2 = 0, 1
        for i in range(2, n + 1):
            tmp = f1 + f2
            f1 = f2
            f2 = tmp
        return f2

