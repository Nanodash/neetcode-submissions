#  [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
# up to n % 3 triplets
# need to maintain the combinations tried (ie. do not count b,a,c if we counted a,b,c)
# brute force seems to work, alternatives must exist
# i notice example output is not the order of brute force
# sort input ascending may help: mirror values
# [-4,-1,-1,0,1,2]
# effective way would be to walk both sides ?
# -4, let's try to cancel it to 0. -4 +2 +1, nope; continue



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 3:
            if sum(nums) == 0:
                res.append(nums)
            return res
        arr = sorted(nums)
        for i, x in enumerate(arr):
            if x > 0: break
            s = []
            s.append(x)
            print(s)
            for j in range(1, 3):
                s.append(arr[- 1 - i])
                print(s)
                if sum(s) > 0: break
            print(s)
            if sum(s) == 0:
                if any(sorted(s) == sorted(r) for r in res): continue
                res.append(s)
        return res
        
        