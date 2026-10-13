# iterate on nums
# maintain last biggest with length
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums.sort()
        res, last = 1, nums[0]
        for n in nums[1:]:
            if n == last + 1:
                last = n
                res += 1
        return res

