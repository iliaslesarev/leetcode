from typing import List, Dict


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        def l_cost(l: str) -> int:
            return ord(l) - 96

        cost_map: Dict[str, int] = {}
        for i in range(len(chars)):
            cost_map[chars[i]] = vals[i]

        cur_cost = max_cost = 0
        for letter in s:
            cur_cost = max(cur_cost + cost_map.get(letter, l_cost(letter)), 0)
            max_cost = max(max_cost, cur_cost)

        return max_cost


print(Solution().maximumCostSubstring(s="abc", chars="abc", vals=[-1, -1, -1]))
print(Solution().maximumCostSubstring(s="adaa", chars="d", vals=[-1000]))
print(Solution().maximumCostSubstring(s="bdbbbbbqccc", chars="dq", vals=[-1, -1000]))
