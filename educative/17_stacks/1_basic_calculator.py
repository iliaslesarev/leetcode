def calculator(s):
    parentheses = []
    number, acc, sign = 0, 0, 1

    for c in s:
        if c.isdigit():
            number = number * 10 + int(c)
        elif c in "-+":
            acc += sign * number
            sign = -1 if c == "-" else 1
            number = 0
        elif c == "(":
            parentheses.append(acc)
            parentheses.append(sign)
            sign = 1
            acc = 0
        elif c == ")":
            acc += sign * number
            acc = acc * parentheses.pop(-1) + parentheses.pop(-1)
            number = 0
    return acc + sign * number


print(calculator("5 + 4 - 1 - 4"))
print(calculator("5 + 4 - (1 - 4)"))
print(calculator("5 + 4 - (1 - 4) + 1"))
print(calculator("5 + 4 - ((1 - 4) + 1)"))
print(calculator("(5 + 4) - (1-3)"))
print(calculator("12 - (6 + 2) + 5"))
print(calculator("(8 + 100) + (13 - 8 - (2 + 1))"))
