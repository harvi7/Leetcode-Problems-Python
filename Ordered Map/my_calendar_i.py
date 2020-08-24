# https://leetcode.com/problems/my-calendar-i/discuss/696179/C%2B%2B-and-Python-solutions

# class MyCalendar:

#     def __init__(self):
#         self.calendar = []

#     def book(self, start: int, end: int) -> bool:
#         for s, e in self.calendar:
#             if s < end and start < e:
#                 return False
#         self.calendar.append((start, end))
#         return True


from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.calendar = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if self.calendar:
            index = self.calendar.bisect_left(start)

            if index != 0 and start < self.calendar.peekitem(index-1)[1]:
                return False

            if index != len(self.calendar) and end > self.calendar.peekitem(index)[0]:
                return False

        self.calendar[start] = end
        return True