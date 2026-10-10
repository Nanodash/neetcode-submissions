class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            if not n in freqs:
                freqs.setdefault(n, 0)
            freqs[n] += 1
    
        ans = []
        for key, value in sorted(freqs.items(), key=lambda item: item[1], reverse=True): 
            ans.append(key)
            if len(ans) == k: break
        return ans