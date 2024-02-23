class Solution(object):
    def romanToInt(self, s):
        symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        prev_value = 0
        for symbol in s:
            value = symbol_values[symbol]
            num += value
            if value > prev_value:
                num -= 2 * prev_value
            prev_value = value
        return num
