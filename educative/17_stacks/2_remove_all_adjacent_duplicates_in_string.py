def remove_adjacent(s: str):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


print(remove_adjacent("aba"))
print(remove_adjacent("aaba"))
print(remove_adjacent("abba"))
print(remove_adjacent("abbdddccca"))
