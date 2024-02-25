class Solution(object):
    def isValid(self, s):
        chars = '(){}[]'
        counts = {c: s.count(c) for c in chars}
        for i in range(0, len(chars),2):
            if counts[chars[i]] != counts[chars[i+1]]:
                return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''
