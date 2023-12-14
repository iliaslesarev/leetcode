def find_duplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# print(find_duplicate([1,5,4,6,2,4,3]))
print(find_duplicate([1, 1]))
