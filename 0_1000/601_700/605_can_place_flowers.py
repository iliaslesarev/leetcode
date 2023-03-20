from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available_places: int = 0
        zeros = 1
        for flower in flowerbed:
            if flower == 0:
                zeros += 1
            elif zeros != 0:
                places, remainder = divmod(zeros, 2)
                if remainder == 0:
                    available_places += places - 1
                else:
                    available_places += places
                zeros = 0
        available_places += zeros // 2

        if available_places >= n:
            return True

        return False


print(Solution().canPlaceFlowers(flowerbed=[1, 1, 1, 0, 0], n=1))
print(Solution().canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1))
