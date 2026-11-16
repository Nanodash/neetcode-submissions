class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(f"mid={mid}")
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        print(f"l={l}, r={r}")

        if target > nums[-1]:
            l, r = 0, mid
        else:
            l, r = mid, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
        