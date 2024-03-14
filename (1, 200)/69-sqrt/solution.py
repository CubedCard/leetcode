class Solution(object):
    def mySqrt(self, x):
        y = 0
        while y * y <= x:
            y += 1
        return y - 1
