class Solution(object):
    def myPow(self, x, n):
        def power(x, n):
            res = x
            for _ in range(n - 1):
                res = res * x
            return res

        if n == 0:
            return 1
        if n > 0:
            return power(x, n)
        if n < 0:
            return 1 / power(x, abs(n))
