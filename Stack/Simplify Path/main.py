class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')

        for component in components:
            if component == ".." and stack:
                stack.pop()
            elif component not in {".", "..", ""}:
                stack.append(component)

        return '/' + '/'.join(stack)