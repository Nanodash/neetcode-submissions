# since e^x * e^y = e^(x+y) and log(e^x) = x
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return math.floor(math.log(math.exp(a)*math.exp(b)))
        