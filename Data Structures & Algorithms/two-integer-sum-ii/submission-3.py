class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(l, r):
            if numbers[l] + numbers[r] > target:
                return search(l, r-1)
            elif numbers[l] + numbers[r] < target:
                return search(l+1, r)
            else:
                return [l + 1, r + 1]

        return search(0, len(numbers) - 1)