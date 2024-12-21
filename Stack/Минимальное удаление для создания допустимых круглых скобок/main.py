class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []

        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')' and stack:
                del stack[-1]
            elif char == ')' and not stack:
                res.append('')
                continue

            res.append(char)

        for i in stack:
            res[i] = ''

        return "".join(res)
