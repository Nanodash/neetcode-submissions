# read through tokens and stack up until operator is found, at which point we reduce stack with the result
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                self.reduce(stack, token)
            else:
                stack.append(token)
        return int(stack[0])

    def reduce(self, stack, token):
        res = int(stack.pop())
        while stack:
            num = int(stack.pop())
            if token == "+":
                res += num
            elif token == "-":
                res -= num
            elif token == "*":
                res = res * num
            elif token == "/":
                res = res // num
        stack.append(str(res))
        