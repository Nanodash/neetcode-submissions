class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charFreqS = {}
        charFreqT = {}
        for c in s:
            charFreqS[c] = charFreqS.get(c, 0) + 1
        for c in t:
            charFreqT[c] = charFreqT.get(c, 0) + 1
        for char in charFreqS:
            if char not in charFreqT:
                return False
            if charFreqT[char] != charFreqS[char]:
                return False
        return True