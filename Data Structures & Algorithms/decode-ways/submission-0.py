# each char should take up to 2 digits
# on each digit, we must consider to take it or group it
# if next is 0, mandatory to group
class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i >= len(s): return 1
            if s[i] == '0': return 0
            elif s[i] == '1':
                return dfs(i + 1) + dfs(i + 2)
            elif s[i] == '2' and i + 1 < len(s):
                return dfs(i + 1) + dfs(i + 2) if int(s[i+1]) < 7 else 0
            else:
                return dfs(i + 1)



        return dfs(0)
        