class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(l, r):
            mid = l + (r - l) // 2
            if numbers[l] + numbers[r] > target:
                return search(l, mid)
            elif numbers[l] + numbers[r] < target:
                return search(mid, r)
            else:
                return [l + 1, r + 1]

        return search(0, len(numbers) - 1)