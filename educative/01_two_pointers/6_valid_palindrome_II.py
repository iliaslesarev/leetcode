def is_palindrome(s):
    def check(ss):
        a, b = 0, len(ss) - 1
        while a < b:
            if ss[a] != ss[b]:
                return False
            a += 1
            b -= 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return check(s[i + 1: j + 1]) or check(s[i:j])
        i += 1
        j -= 1
    return True


print(is_palindrome("qwecq"))
