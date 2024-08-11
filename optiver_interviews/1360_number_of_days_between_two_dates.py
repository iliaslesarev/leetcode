class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def count_days(date):
            months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days = 0

            year, month, day = [int(number) for number in date.split("-")]

            for y in range(1900, year):
                if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                    days += 366
                else:
                    days += 365

            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                months[2] = 29

            days += sum(months[:month]) + day
            return days

        return abs(count_days(date1) - count_days(date2))

    def daysInMonth(self, year: int, month: int):
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            months[2] = 29
        return months[month]

print(Solution().daysBetweenDates("2020-01-15", "2019-12-31"))
# print(Solution().daysBetweenDates("1901-02-02", "2019-12-31"))
# print(Solution().daysBetweenDates("2019-06-29", "2019-06-30"))
