# [[1,3],[1,5],[6,7]]
# [1, 3], we set current interval
# [1, 5], overlap
# this example works since it's sorted, i assume we need that
# since it's sorted, we can only merge consecutive intervals, the time complexity trade-off seems worth it.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        curr = intervals[0]
        for interval in sorted(intervals, key=lambda i: i[0]):
            if interval[0] <= curr[1]:
                curr = [curr[0], interval[1]]
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res
        