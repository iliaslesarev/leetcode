def min_window(str1, str2):
    i = j = 0
    result = ""
    while i < len(str1):
        if str1[i] == str2[j]:
            j += 1

        if j == len(str2):
            j -= 1
            start, end = i, i
            while j >= 0:
                if str1[i] == str2[j]:
                    j -= 1
                if j == -1:
                    start = i

                i -= 1

            if result == "":
                result = str1[start:end + 1]
            elif len(result) > (end + 1 - start):
                result = str1[start:end + 1]
            i = start
            j = 0
        i += 1

    return result


print(min_window("abcdebdde", "bde"))
print(min_window("afgegrwgwga", "aa"))
print(min_window("abcdbebe", "bbe"))
