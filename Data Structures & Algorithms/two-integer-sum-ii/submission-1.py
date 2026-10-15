# a solution would be to make a two pointer loop: fixing i and checking which j makes up target
# o(n^2), we need to optimize since there may be up to 30k numbers
# a binary search may be better in most cases (o(n))
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] != numbers[j] and numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        return []