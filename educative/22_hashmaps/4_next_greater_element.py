def next_greater_element(nums1, nums2):
    greater_map = {}
    helper_stack = []

    for n in nums2:
        while len(helper_stack) != 0 and n > helper_stack[-1]:
            greater_map[helper_stack.pop(-1)] = n
        helper_stack.append(n)

    for n in helper_stack:
        greater_map[n] = -1

    return [greater_map[n] for n in nums1]

# print(next_greater_numbers([5, 4, 7], [4, 5, 7, 3]))
print(next_greater_element([137,59,92,122,52,131,79,236] , [137,59,92,122,52,131,79,236]))