def space_replace(arr):
    space_amount = 0
    for el in arr:
        if el == " ":
            space_amount += 1

    first = len(arr) - 1
    arr += [""] * space_amount * 2
    second = len(arr) - 1

    while first >= 0:
        if arr[first] != " ":
            arr[second] = arr[first]
            second -= 1
        else:
            arr[second] = "0"
            arr[second - 1] = "2"
            arr[second - 2] = "%"
            second -= 3
        first -= 1

    return arr

# %20
a = ["q", " ", "z", "x", "c", " ", "q", "w", "e", " ", " "]
print(a)
print(space_replace(a))