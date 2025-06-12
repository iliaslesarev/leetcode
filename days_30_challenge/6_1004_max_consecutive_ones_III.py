from typing import List


def find_ones(nums: List[int], k: int) -> int:
    start = end = max_size = 0
    zeros = k

    while end < len(nums):
        if nums[end] == 0:
            zeros -= 1

        while zeros < 0:
            if nums[start] == 0:
                zeros += 1
            start += 1

        max_size = max(max_size, end - start + 1)
        end += 1

    return max_size


print(find_ones(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(find_ones(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
print(find_ones(nums=[0, 0, 0, 1, 1, 1], k=1))
