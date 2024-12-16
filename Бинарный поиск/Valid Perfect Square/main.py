class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num + 1

        while r - l > 1:
            m = (l+r) // 2

            if m ** 2 <= num:
                l = m
            else:
                r = m

        return True if l ** 2 == num else False