class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i):
            if i >= len(nums): return 0
            skip = dfs(i + 1)
            rob = nums[i] + dfs(i + 2)
            return max(skip, rob)
        return dfs(0)
