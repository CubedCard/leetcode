class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        pos_or_neg = 1
        if s[0] in ['+', '-']:
            if s[0] == '-':
                pos_or_neg = -1
            s = s[1:]
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        num = num * pos_or_neg
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num

