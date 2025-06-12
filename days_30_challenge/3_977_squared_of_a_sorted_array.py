from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n

    left, right = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result


print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))
print(sortedSquares([-1]))
print(sortedSquares([-5, -3, -2, -1]))
