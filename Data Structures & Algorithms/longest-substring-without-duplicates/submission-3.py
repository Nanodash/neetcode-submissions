class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        i = 0
        res = 1
        curr = s[0]
        while i < len(s) - 1:
            if s[i + 1] not in curr:
                i += 1
                curr += s[i]
            else:
                curr = curr[1:]
            res = max(res, len(curr)) 
        return res
