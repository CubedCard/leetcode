import sys

sys.setrecursionlimit(1000)

class Solution(object):
    def isHappy(self, n):
        if n == 1:
            return True
        res = 0
        for x in str(n):
            res += int(x)**2
        try:
            return self.isHappy(res)
        except Exception:
            return False
