def is_happy_number(n):
    def get_square_sum(number):
        sum = 0
        while number != 0:
            sum += (number % 10) ** 2
            number //= 10
        return sum

    a = b = n
    while True:
        a = get_square_sum(a)
        b = get_square_sum(get_square_sum(b))
        if b == 1:
            return True
        elif a == b:
            return False


print(is_happy_number(28))
print(is_happy_number(4))
print(is_happy_number(7))
