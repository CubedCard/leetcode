class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            return any(char.isdigit() for char in s)
        except ValueError:
            return False
