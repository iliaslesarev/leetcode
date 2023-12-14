def find_repeated_sequences(s, k):
    alphabet = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    hash_sum = 0
    for i in range(k):
        hash_sum += alphabet.get(s[i]) * 4 ** (k - i - 1)

    visited = set()
    visited_hashes = {hash_sum}

    for i in range(k, len(s)):
        hash_sum -= alphabet.get(s[i - k]) * 4 ** (k - 1)
        hash_sum *= 4
        hash_sum += alphabet.get(s[i])

        if hash_sum in visited_hashes:
            visited.add(s[i - k + 1:i + 1])
        else:
            visited_hashes.add(hash_sum)

    return visited_hashes


print(find_repeated_sequences("AAAAACCCCCAAAAACCCCCC", 3))
print(find_repeated_sequences("TTTTTGGGTTTTCCA", 14))
