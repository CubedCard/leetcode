class Solution(object):
    def reverse(self, x):
        s = str(x)
        mul = 1 if s[0] != '-' else -1
        s = s[1:] if s[0] == '-' else s
        rev = s[::-1]
        return mul * int(rev) if -2**31 <= int(rev) <= 2**31 - 1 else 0
