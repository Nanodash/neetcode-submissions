# read through tokens and stack up until operator is found, at which point we reduce stack with the result
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                self.reduce(stack, token)
            else:
                stack.append(int(token))
        return stack[0]

    def reduce(self, stack, token):
        num2 = stack.pop()
        num1 = stack.pop()
        if token == "+":
            res = num1 + num2
        elif token == "-":
            res = num1 - num2
        if token == "*":
            res = num1 * num2
        if token == "/":
            res = num1 // num2
        stack.append(res)
        