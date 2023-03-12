class Solution:
    def decodeString(self, s: str) -> str:
        stack, number, cur_line = [], [], []

        for l in s:
            if l.isdigit():
                number.append(l)
            elif l == "[":
                stack.append(cur_line)
                stack.append(number)
                number, cur_line = [], []
            elif l == "]":
                cur_number = stack.pop()
                prev_line = stack.pop()
                cur_line = ["".join(prev_line) + "".join(cur_line) * int("".join(cur_number))]
            else:
                cur_line.append(l)
        return "".join(cur_line)


print(Solution().decodeString(s="3[a]2[bc]") == "aaabcbc")
print(Solution().decodeString(s="3[a2[c]]") == "accaccacc")
print(Solution().decodeString(s="2[abc]3[cd]ef") == "abcabccdcdcdef")
