class Solution(object):
    def intToRoman(self, num):
        symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        roman = ""
        for symbol in "MDCLXVI":
            value = symbol_values[symbol]
            while num >= value:
                num -= value
                roman += symbol
            if num == 0:
                break
            next_symbol = "I" if symbol == "X" else "X" if symbol == "C" else "C" if symbol == "M" else ""
            next_symbol = "I" if symbol == "V" else "X" if symbol == "L" else "C" if symbol == "D" else next_symbol
            next_value = symbol_values[next_symbol]
            if num >= value - next_value:
                num -= value - next_value
                roman += next_symbol + symbol
        return roman
