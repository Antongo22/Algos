from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for index, token in enumerate(tokens):
            if token.lstrip("-").isdigit():
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))

        return stack[0]

new = Solution()
new.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])