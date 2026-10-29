class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, r = 0, 0
        res = 1
        curr = s[0]
        while r < len(s) - 1:
            if s[r + 1] not in curr:
                r += 1
                curr += s[r]
            else:
                l += 1
                curr = curr[1:]
            res = max(res, len(curr)) 
        return res
