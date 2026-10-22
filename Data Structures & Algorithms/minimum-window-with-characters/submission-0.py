# iterate over s, each time a char from t is found that's a candidate for substring start
# on each candidate, try to find the substring
# return the shortest of the substrings found

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        candidates = []
        for i, c in enumerate(s):
            if c in t:
                j = i
                candidate = ""
                while not(Counter(t) <= Counter(candidate)) and j <= len(s) - 1:
                    candidate += s[j]
                    j += 1
                if Counter(t) <= Counter(candidate):
                    candidates.append(candidate)
        return min(candidates, key=len, default="")