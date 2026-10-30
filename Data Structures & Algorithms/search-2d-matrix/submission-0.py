# since values are sorted, we can create a 1D array from the 2D matrix and use binary search to optimize the target lookup
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten = []
        for row in matrix:
            flatten += row
        l, r = 0, len(flatten) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if flatten[mid] > target:
                r = mid - 1
            elif flatten[mid] < target:
                l = mid + 1
            else: return True
        return False