from typing import List


def find_subarray(nums: List[int], k: int):
    max_avg = avg = sum(nums[0:k]) / k
    for i in range(len(nums) - k):
        avg = (avg * k - nums[i] + nums[i + k]) / k
        max_avg = max(avg, max_avg)
    return max_avg


print(find_subarray(nums=[1, 12, -5, -6, 50, 3], k=4))
print(find_subarray(nums=[5], k=1))
print(find_subarray(nums=[1, 2, 3, 5], k=2))
