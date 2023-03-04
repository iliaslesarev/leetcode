from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def helper(new_sr: int, new_sc: int):
            if (
                    0 <= new_sr < len(image) and
                    0 <= new_sc < len(image[0]) and
                    image[new_sr][new_sc] == initial_color
            ):
                image[new_sr][new_sc] = color
                helper(new_sr - 1, new_sc)
                helper(new_sr + 1, new_sc)
                helper(new_sr, new_sc - 1)
                helper(new_sr, new_sc + 1)

        initial_color: int = image[sr][sc]
        if initial_color != color:
            helper(sr, sc)
        return image


# print(Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
print(Solution().floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))
