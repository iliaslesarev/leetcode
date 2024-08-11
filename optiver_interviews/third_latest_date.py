from datetime import date, datetime
from typing import List
import heapq


class Solution:
    def third_latest_date(self, dates: List[str]):
        dates = [-datetime.strptime(day, "%Y-%m-%d").timestamp() for day in dates]
        print(heapq.heapify(dates))

        print(heapq.heappop(dates))
        print(heapq.heappop(dates))
        return datetime.fromtimestamp(-heapq.heappop(dates))


print(Solution().third_latest_date(["2022-01-01", "2024-06-06", "2022-03-03", "2099-03-04"]))
#
#
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         s_nums = set(nums)
#         heap_nums = [-num for num in s_nums]
#         heapq.heapify(heap_nums)
#
#         maximum = heapq.heappop(heap_nums)
#
#         if len(heap_nums) > 0:
#             heapq.heappop(heap_nums)
#         if len(heap_nums) > 0:
#             return -heapq.heappop(heap_nums)
#         else:
#             return -maximum


# print(Solution().thirdMax([3, 2, 1]))
# print(Solution().thirdMax([1, 2]))
# print(Solution().thirdMax([2, 2, 3, 1]))
