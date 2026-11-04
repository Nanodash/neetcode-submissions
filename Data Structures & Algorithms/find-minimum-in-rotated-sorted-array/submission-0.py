class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

        