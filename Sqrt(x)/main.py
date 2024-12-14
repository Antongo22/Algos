class Solution:
    def good(self, num, target):
        return num ** 2 <= target

    def mySqrt(self, x: int) -> int:

        l, r = 0, x + 1

        while r - l > 1:
            mid = (r + l) // 2

            if self.good(mid, x):
                l = mid
            else:
                r = mid

        return l
