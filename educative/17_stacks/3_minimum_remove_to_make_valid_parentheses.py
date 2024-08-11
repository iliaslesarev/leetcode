def make_valid_parentheses(s: str):
    removed = []
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                removed.append(i)
    s = [elem for i, elem in enumerate(s) if i not in removed and i not in stack]

    return "".join(s)


print(make_valid_parentheses("(aa)"))
print(make_valid_parentheses("(aa))"))
print(make_valid_parentheses(")(aa)"))
print(make_valid_parentheses("(a(b)c)aaa()"))
print(make_valid_parentheses("(a(b)c)aaa)("))
