class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            sq_sum = 0
            while number > 0:
                number, remainder = divmod(number, 10)
                sq_sum += remainder ** 2
            return sq_sum

        turtle, rabbit = n, get_next(n)

        while rabbit != turtle and rabbit != 1:
            rabbit = get_next(get_next(rabbit))
            turtle = get_next(turtle)

        return rabbit == 1


print(Solution().isHappy(n=19))
print(Solution().isHappy(n=2))
print(Solution().isHappy(n=3))
