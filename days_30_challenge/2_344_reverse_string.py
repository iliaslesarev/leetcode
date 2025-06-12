def reverse_string(s):
    first, second = 0, len(s) - 1
    while first < second:
        s[first], s[second] = s[second], s[first]
        first += 1
        second -= 1
    return s

s = ["h","e","l","l","o"]
print(reverse_string(s))
s = ["h"]
print(reverse_string(s))
s = []
print(reverse_string(s))
