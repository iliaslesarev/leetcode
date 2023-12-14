def min_sub_array_len(target, nums):
    left = curr_sum = 0
    minimum_length = len(nums) + 1
    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            minimum_length = min(minimum_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    if minimum_length == len(nums) + 1:
        return 0
    return minimum_length


print(min_sub_array_len(6, [1, 2, 3, 4, 5]))
print(min_sub_array_len(6, [1, 2, 3, 6, 5]))
print(min_sub_array_len(6, [1, 2, 2, 4, 5]))
print(min_sub_array_len(6, [6]))
print(min_sub_array_len(6, [6, 6, 6]))
