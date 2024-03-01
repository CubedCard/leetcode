class Solution(object):
    def maximumOddBinaryNumber(self, s):
        number_of_zeros = s.count('0')
        number_of_ones = len(s) - number_of_zeros
        if number_of_ones == 0:
            return ""
        return '1' * (number_of_ones - 1) + '0' * number_of_zeros + '1'
