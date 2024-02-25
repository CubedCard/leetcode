class Solution(object):
    def letterCombinations(self, digits):
        digits = [int(x) for x in digits]

        if 0 >= len(digits) or len(digits) > 4:
            return []
        if any(2 > x > 9 for x in digits):
            return []
        
        phone_chars = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        chars = [phone_chars[num] for num in digits]

        return [''.join(x) for x in itertools.product(*chars)]
