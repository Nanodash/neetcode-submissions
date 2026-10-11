class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1
        i = 0
        while i < lastIndex:
            jump = nums[i]
            if jump == 0: break
            i += jump
        return i >= lastIndex
        