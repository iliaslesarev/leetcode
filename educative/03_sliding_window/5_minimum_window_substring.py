def min_window(s, t):
    if s == t:
        return t

    freq_map = {}
    for char in t:
        freq_map[char] = freq_map.get(char, 0) + 1

    start = end = 0
    minimum_length, minimum_line = len(s), ""
    required = len(freq_map.keys())

    while end < len(s):
        if s[end] in freq_map:
            freq_map[s[end]] -= 1
            if freq_map[s[end]] == 0:
                required -= 1

        while required == 0:
            if end - start + 1 <= minimum_length:
                minimum_length = end - start + 1
                minimum_line = s[start:end + 1]

            if s[start] in freq_map.keys():
                freq_map[s[start]] += 1
                if freq_map[s[start]] == 1:
                    required += 1
            start += 1
        end += 1

    return minimum_line


print(min_window("cabwefgewcwaefgcf", "cae"))
print(min_window("bbaac", "aba"))
print(min_window("AbabbbAbaA", "Bab"))
print(min_window("ABXYZJKLSNFC", "ABC"))
print(min_window("ABDFGDCKAB", "ABCD"))