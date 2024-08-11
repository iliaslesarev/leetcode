class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_len = 0
        visited = {}

        while right < len(s):
            if s[right] not in visited or visited[s[right]] < left:
                visited[s[right]] = right
            else:
                max_len = max(max_len, right - left - 1)
                left += 1
            right += 1

        return max_len

print(Solution().lengthOfLongestSubstring(" "))