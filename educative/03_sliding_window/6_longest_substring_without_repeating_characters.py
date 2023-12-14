def find_longest_substring(input_str):
    visited_characters = {}
    start = max_size = 0

    for end in range(len(input_str)):
        if input_str[end] in visited_characters:
            start = max(start, visited_characters[input_str[end]] + 1)

        visited_characters[input_str[end]] = end
        max_size = max(max_size, end - start + 1)

    return max_size

# print(find_longest_substring("abcdbceeee"))
# print(find_longest_substring(""))
# print(find_longest_substring("eee"))
print(find_longest_substring("abcdbea"))