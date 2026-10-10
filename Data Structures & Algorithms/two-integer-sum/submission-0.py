
# find index i and j that sums to target
# nums[i] + nums[j] = target
# find index j that equals target - index i
# nums[j] = target - nums[i]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cache:
                return [cache[diff], i]
            cache[nums[i]] = i
        raise Exception("unexpected result")


        