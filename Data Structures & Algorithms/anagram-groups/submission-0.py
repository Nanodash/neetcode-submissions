class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _anagrams = {}
        for s in strs:
            freqs = [0] * 26
            for c in s:
                freqs[ord(c) - ord("a")] = freqs[ord(c) - ord("a")] + 1
            key = tuple(freqs)
            if key not in _anagrams:
                _anagrams[key] = []
            _anagrams[key].append(s)
        return list(_anagrams.values())