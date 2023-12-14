class Solution:
    def removePalindromeSub(self, s: str) -> int:
        res = 0
        arr = list(s)
        while len(arr) != 0:
            i = 0
            if len(arr) == 1:
                del arr[0]
            else:
                while i < len(arr) - 1:
                    if arr[i] == arr[len(arr) - 1]:
                        del arr[i]
                        del arr[len(arr) - 1]
                    else:
                        i += 1
            res += 1
        return res


print(Solution().removePalindromeSub(s = "baabb"))

# baabbaabbab
# aabbaabba
# abbaabb
# abbaa bb
# bba bb
# a bb
