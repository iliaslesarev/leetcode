def is_subsequence(s, t):
    first = second = 0
    while first < len(s):
        if second >= len(t):
            return False

        if s[first] == t[second]:
            first += 1
        second += 1
    return True

s, t = "abc", "ahbgdc"
print(is_subsequence(s, t))
s, t = "axc", "ahbgdc"
print(is_subsequence(s, t))


