class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        i, j = 0, 1
        while j < len(s):
            sub = s[i: j + 1]
            freq = self._getFreq(sub)
            swaps = len(sub) - max(freq.values())
            if swaps <= k: res = len(sub)
            else: i+=1
            j+=1

        return res

    def _getFreq(self, s):
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        return freq
            
        