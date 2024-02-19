class Solution(object):
    def convert(self, s, numRows):
        if 1 > len(s) > 1000:
            return ''
        if 1 > numRows > 1000:
            return ''
        if numRows == 1:
            return s
        result = ''
        for i in range(numRows):
            j = i
            while j < len(s):
                result += s[j]
                if i != 0 and i != numRows - 1:
                    if j + 2 * (numRows - i - 1) < len(s):
                        result += s[j + 2 * (numRows - i - 1)]
                j += 2 * numRows - 2
        return result

