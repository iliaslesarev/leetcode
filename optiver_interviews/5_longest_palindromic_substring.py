# O(n^3)
def longestPalindrome2(s: str) -> str:
    # O(n)
    def is_palindrome(ss):
        length = len(ss)
        for i in range(length // 2):
            if ss[i] != ss[length - i - 1]:
                return False
        return True

    # O(n^2)
    for window_size in range(len(s), 0, -1):
        for i in range(len(s) - window_size + 1):
            if is_palindrome(s[i:i + window_size]):
                return s[i:i + window_size]

    return ""


# O(n^2). memory O(n^2)
def longestPalindrome3(s: str) -> str:
    answer = [0, 0]
    checks = []

    for i in range(len(s)):
        arr = [False] * len(s)
        arr[i] = True

        if i != len(s) - 1 and s[i] == s[i + 1]:
            arr[i + 1] = True
            answer = [i, i + 1]

        checks.append(arr)

    for k in range(len(s)):
        for i in range(len(s) - k - 1):
            j = i + k + 1

            if s[i] == s[j] and checks[i + 1][j - 1]:
                checks[i][j] = True
                answer = [i, j]

    return s[answer[0]:answer[1] + 1]


# O(n^2). memory O(1)
def longestPalindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    answer = [0, 0]

    for i in range(len(s)):
        # odd
        new_left, new_right = expand(i, i)
        if new_right - new_left > answer[1] - answer[0] >= 0:
            answer = [new_left, new_right]

        # even
        new_left, new_right = expand(i, i + 1)
        if new_right - new_left > answer[1] - answer[0] >= 0:
            answer = [new_left, new_right]

    return s[answer[0]:answer[1] + 1]


print(longestPalindrome("cbbd"))
print(longestPalindrome("babad"))
print(longestPalindrome("abc"))
print(longestPalindrome("aba"))
print(longestPalindrome("abba"))
print(longestPalindrome("cabac"))
print(longestPalindrome("cabbad"))
print(longestPalindrome("cacdac"))
