class Solution:
    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     def get_stack(line: str) -> []:
    #         res = []
    #         for l in line:
    #             if l != "#":
    #                 res.append(l)
    #             elif res:
    #                 res.pop()
    #         return res
    #
    #     return get_stack(s) == get_stack(t)

    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j, hashes = len(s) - 1, len(t) - 1, 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    hashes += 1
                    i -= 1
                elif hashes != 0:
                    hashes -= 1
                    i -= 1
                else:
                    break
            hashes = 0
            while j >= 0:
                if t[j] == "#":
                    hashes += 1
                    j -= 1
                elif hashes != 0:
                    hashes -= 1
                    j -= 1
                else:
                    break

            if (i >= 0 and j >= 0 and s[i] != t[j]) or ((i >= 0) != (j >= 0)):
                return False
            else:
                j -= 1
                i -= 1

        return True


print(Solution().backspaceCompare(s="ab#c", t="ad#c") == True)
print(Solution().backspaceCompare(s="ab##", t="c#d#") == True)
print(Solution().backspaceCompare(s="a#c", t="b") == False)
print(Solution().backspaceCompare(s="a##c", t="#a#c") == True)
print(Solution().backspaceCompare(s="bbbextm", t="bbb#extm") == False)
print(Solution().backspaceCompare(s="xywrrmp", t="xywrrmu#p") == True)
print(Solution().backspaceCompare(s="a#c###", t="ad#c") == False)
