class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        chars = {'(' : ')',
                 '{' : '}',
                 '[' : ']'}


        for i in s:
            if i in chars:
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if chars[last] != i:
                    return False
        return len(stack) == 0


