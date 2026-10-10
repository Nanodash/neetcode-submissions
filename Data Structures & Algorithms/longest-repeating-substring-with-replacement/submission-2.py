class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        i = 0
        count = defaultdict(int)
        maxf = 0
        for j in range(len(s)):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            if (j - i + 1) - maxf > k: 
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)

        return res
  