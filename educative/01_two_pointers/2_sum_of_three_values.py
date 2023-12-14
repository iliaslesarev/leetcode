def find_sum_of_three(nums, target):
    nums.sort()

    for i in range(0, len(nums) - 2):
        low, high = i + 1, len(nums) - 1

        while low < high:
            summ = nums[i] + nums[low] + nums[high]

            if summ == target:
                return True
            elif summ > target:
                high -= 1
            else:
                low += 1
    return False
