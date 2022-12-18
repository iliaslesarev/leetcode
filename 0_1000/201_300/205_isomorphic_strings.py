from typing import Dict, Set
import string


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionary: Set[str] = set(string.printable)

        dict_map: Dict[str, str] = dict()
        for i in range(len(t)):
            if not dict_map.get(t[i]) and s[i] in dictionary:
                dict_map[t[i]] = s[i]
                dictionary.remove(s[i])
            if dict_map.get(t[i]) != s[i]:
                return False

        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s_t: Dict[str, str] = dict()
        dict_t_s: Dict[str, str] = dict()

        for i in range(len(s)):
            if not dict_s_t.get(s[i]) and not dict_t_s.get(t[i]):
                dict_s_t[s[i]] = t[i]
                dict_t_s[t[i]] = s[i]
            elif dict_s_t.get(s[i]) != t[i] or dict_t_s.get(t[i]) != s[i]:
                return False

        return True


print(Solution().isIsomorphic2(s="foo", t="bar"))
