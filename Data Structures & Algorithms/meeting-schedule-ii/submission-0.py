"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# each time two intervals overlap, we must add a room. when first interval ends, that room is free.
# each room can be considered as a queue, we append non overlapping intervals to each, adding a slot/room each time overlap is found.
# sorting cannot be used since they are up to 100k intervals.
# we can use maxheap to get the max time a room is at in O(1); it implies extracting only endtime but it would be error prone, what if start time is close?
# so we need to extract both start and end times
# Time: O(nlog(n)) (sorting) + O(n) (traversal) = O(nlog(n))
# Space: O(n)*2 = O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        if len(intervals) == 1: return 1
        startTimes = [i.start for i in intervals]
        startTimes.sort()
        endTimes = [i.end for i in intervals]
        endTimes.sort()
        count = 0
        res = 0
        s, e = 0, 0 # positions in start and end arrays
        while s < len(startTimes) and e < len(endTimes):
            # if current meeting is not ended, we must add a room
            if startTimes[s] < endTimes[e]:
                count += 1
                s += 1
            else:
                # a room is free
                count -= 1
                e += 1
            res = max(res, count)
        return res



        