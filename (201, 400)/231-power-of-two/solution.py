class Solution(object):
    def isPowerOfTwo(self, n):
        powers = [2**i for i in range(31)]
        return n in powers

