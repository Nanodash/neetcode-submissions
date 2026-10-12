class Solution:
    def rob(self, nums: List[int]) -> int:
        oddTotal = evenTotal = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                evenTotal += nums[i]
            else:
                oddTotal += nums[i]
        return max(oddTotal, evenTotal)
        