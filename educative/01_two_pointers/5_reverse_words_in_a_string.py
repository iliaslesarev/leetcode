def reverse_words(sentence):
    def reverse_word(word):
        i, j = 0, len(word) - 1
        res = [""] * len(word)
        while i <= j:
            res[i] = word[j]
            res[j] = word[i]
            i += 1
            j -= 1
        return "".join(res)

    sentence = sentence[::-1]
    result = []
    i = j = 0
    while j < len(sentence):
        if sentence[j] == " " and i == j:
            i = j + 1
        elif sentence[j] == " ":
            result.append(reverse_word(sentence[i:j]))
            i = j + 1
        elif j == len(sentence) - 1:
            result.append(reverse_word(sentence[i:j + 1]))
        j += 1

    return " ".join(result)

print(reverse_words("Hello     World"))
