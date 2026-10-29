# we maintain a sliding window and count per char map. expand to right until duplicate char, in which case we shrink from left.
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, r = 0, 0
        res = 1
        curr = 1
        count = {s[0]: 1}
        while r + 1 < len(s):
            if count.get(s[r + 1], 0) == 0:
                r += 1
                count[s[r]] = count.get(s[r], 0) + 1
                curr += 1
            else:
                count[s[l]] = count[s[l]] - 1
                l += 1
                curr -= 1
            res = max(res, curr) 
        return res
