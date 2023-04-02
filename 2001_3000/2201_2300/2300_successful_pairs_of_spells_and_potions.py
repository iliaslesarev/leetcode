from typing import List, Dict


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        spells = [(spell, i) for i, spell in enumerate(spells)]
        spells.sort()
        potions.sort()
        result = [-1] * len(spells)

        success_min_index = len(potions) - 1
        for spell in spells:
            while spell[0] * potions[success_min_index] >= success and success_min_index >= 0:
                success_min_index -= 1
            result[spell[1]] = len(potions) - success_min_index - 1

        return result


print(
    Solution().successfulPairs(spells=[20, 26, 38, 23, 23, 20, 14, 30], potions=[24, 1, 7, 26, 19, 17, 7], success=510))
