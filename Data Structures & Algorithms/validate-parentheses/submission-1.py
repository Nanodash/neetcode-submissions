class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = deque()
        bracketMap = {"{":"}", "[":"]", "(":")"}
        for c in s:
            if len(stack) == 0 and c not in bracketMap:
                return False
            if c in bracketMap:
                stack.append(c)
            elif c != bracketMap[stack[-1]]:
                return False
            else:
                stack.pop()
        return len(stack) == 0


        