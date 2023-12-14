def sort_colors(colors):
    left, middle, right = 0, 0, len(colors) - 1
    while middle <= right:
        if colors[middle] == 0:
            if colors[left] == 0:
                middle += 1
            else:
                tmp = colors[left]
                colors[left] = colors[middle]
                colors[middle] = tmp
            left += 1
        elif colors[middle] == 2:
            if colors[right] == 2:
                right -= 1
            else:
                tmp = colors[middle]
                colors[middle] = colors[right]
                colors[right] = tmp
                right -= 1
        else:
            middle += 1

    return colors


print(sort_colors([1, 1, 1, 2, 2, 0, 0, 2, 1]))
print(sort_colors([1, 0, 2, 1, 0, 1, 1, 2]))
