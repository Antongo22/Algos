class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        for char in A:
            if char == "(":
                count += 1
            elif count > 0:
                count -= 1
            else:
                return 0

        return 1 if count == 0 else 0