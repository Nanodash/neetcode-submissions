class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prex = [1] * n
        for i in range(1, n):
            prex[i] = prex[i - 1] * nums[i - 1]

        sufx = [1] * n
        for i in range(n - 2, -1, -1):
            sufx[i] = sufx[i + 1] * nums[i + 1]

        products = [1] * n
        for i in range(0, n):
            products[i] = prex[i] * sufx[i]
        return products
