class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums): return 0
            if mem[i] != -1: return mem[i]
            skip = dfs(i + 1)
            rob = nums[i] + dfs(i + 2)
            mem[i] = max(skip, rob)
            return mem[i]
        return dfs(0)
