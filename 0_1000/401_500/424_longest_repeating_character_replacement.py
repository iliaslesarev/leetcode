from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = max_freq = longest_substring = 0
        freq_map = {}
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            max_freq = max(max_freq, freq_map[s[end]])

            is_valid = end + 1 - start - max_freq <= k
            if not is_valid:
                freq_map[s[start]] -= 1
                start += 1

            longest_substring = end + 1 - start

        return longest_substring


print(Solution().characterReplacement(s="ABAA", k=0) == 2)
print(Solution().characterReplacement(s="BAAAB", k=2))
print(Solution().characterReplacement(s="ABAB", k=2) == 4)
print(Solution().characterReplacement(s="AABABBA", k=1) == 4)
print(Solution().characterReplacement(s="BAAA", k=0) == 3)
print(Solution().characterReplacement(s="ABBB", k=2) == 4)
