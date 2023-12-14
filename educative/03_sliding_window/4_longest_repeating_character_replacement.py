def longest_repeating_character_replacement(s, k):
    flagged_characters = {}
    start = end = maximum_length = maximum_frequency = 0

    while end < len(s):
        if s[end] not in flagged_characters:
            flagged_characters[s[end]] = 1
        else:
            flagged_characters[s[end]] += 1

        maximum_frequency = max(maximum_frequency, flagged_characters[s[end]])

        if end - start + 1 > maximum_frequency + k:
            flagged_characters[s[start]] -= 1
            start += 1

        maximum_length = max(maximum_length, end - start + 1)
        end += 1

    return maximum_length


print(longest_repeating_character_replacement("aabccbb", 2))
print(longest_repeating_character_replacement("aaaaaaaaaab" , 2))
print(longest_repeating_character_replacement("aaaaaaaaaa" , 2))
print(longest_repeating_character_replacement("ccabdf" , 1))
