from typing import List


def total_fruit(fruits: List[int]) -> int:
    collected_fruits = {}
    start = end = total = collected_fruits_amount = 0

    while end < len(fruits):
        if fruits[end] in collected_fruits or len(collected_fruits.keys()) < 2:
            collected_fruits[fruits[end]] = collected_fruits.get(fruits[end], 0) + 1
            collected_fruits_amount += 1
            end += 1
        else:
            total = max(total, collected_fruits_amount)
            collected_fruits[fruits[start]] -= 1
            collected_fruits_amount -= 1
            if collected_fruits[fruits[start]] == 0:
                del collected_fruits[fruits[start]]
            start += 1

    return max(total, collected_fruits_amount)

print(total_fruit(fruits = [1,2,1]))
print(total_fruit(fruits = [0,1,2,2]))
print(total_fruit(fruits = [1,2,3,2,2]))
print(total_fruit(fruits = [0, 0, 0, 0]))
