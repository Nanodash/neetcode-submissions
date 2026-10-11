class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        curr = sorted_intervals[0]
        for interval in sorted_intervals:
            if interval[0] <= curr[1]:
                curr = [curr[0], interval[1] if interval[1] > curr[1] else curr[1]]
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res
        