"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#[(5,10),(0,30),(15,20)]

# to avoid conflicts, interval must not overlap. since no order is guaranteed, we may sort the array to simplify. It allows us to iterate over sorted array and verify end_i <= start_j
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True
