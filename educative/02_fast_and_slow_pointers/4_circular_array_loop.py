def circular_array_loop(nums):
    amount = len(nums)
    for i in range(amount):
        slow = fast = i

        while True:
            next_slow = (slow + nums[slow]) % amount
            next_fast = (fast + nums[fast]) % amount
            if nums[next_slow] * nums[slow] < 0 or nums[next_fast] * nums[fast] < 0:
                break
            if next_slow == slow:
                return False
            fast = next_fast
            next_fast = (fast + nums[fast]) % amount
            if nums[next_fast] * nums[fast] < 0:
                break

            slow = next_slow
            fast = next_fast
            if slow == fast:
                return True

    return False


print(circular_array_loop([3, 3, 1, -1, 2]))
print(circular_array_loop([1, 3, -2, -4, 1]))
print(circular_array_loop([2, 1, -1, -2]))
