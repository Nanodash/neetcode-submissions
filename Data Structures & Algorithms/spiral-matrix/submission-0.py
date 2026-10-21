# iterate and keep latest turn to be able to continue turning clockwise when reaching an already visited slot or matrix boundary
# if direction down: go 1 row down on same col
# if direction left: stay on row and iterate backward
# if direction up: go 1 row up on same col
# if direction right: stay on row and iterate forward
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)

        def canContinue():
            return l < r and t < b

        while canContinue():
            for i in range(l, r):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
            if not canContinue(): break

            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
            for i in range(b-1,t-1, -1):
                res.append(matrix[i][l])
            l+=1


        return res