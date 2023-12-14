from collections import deque


def find_max_sliding_window(nums, w):
    def cleanup(window, index, arr):
        while window and arr[window[-1]] < arr[index]:
            window.pop()

    if w > len(nums):
        return max(nums)

    current_window = deque()
    result = []

    for i in range(w):
        cleanup(current_window, i, nums)
        current_window.append(i)
    result.append(nums[current_window[0]])

    for i in range(w, len(nums)):
        cleanup(current_window, i, nums)
        current_window.append(i)
        if i - current_window[0] > w - 1:
            current_window.popleft()
        result.append(nums[current_window[0]])

    return result


print(find_max_sliding_window([10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67], 3))
