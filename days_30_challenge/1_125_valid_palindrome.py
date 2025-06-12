def is_palindrome(s):
    check_symbols = "qwertyuiopasdfghjklzxcvbnm0123456789"
    start, end = 0, len(s) - 1

    while start < end:
        if s[start].lower() not in check_symbols:
            start += 1
        elif s[end].lower() not in check_symbols:
            end -= 1
        elif s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1

    return True

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
s = "race a car"
print(is_palindrome(s))
s = " "
print(is_palindrome(s))
s = ".,"
print(is_palindrome(s))
s = "0P"
print(is_palindrome(s))
